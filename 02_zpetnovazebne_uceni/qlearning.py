import gymnasium
import numpy as np
import utils
import matplotlib.pyplot as plt


class QAgent:
    def __init__(self, action_space, epsilon=0.01, alpha=0.1, gamma=0.9):
        self.action_space = action_space
        
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        
        num_bins_position = 12 # 12 subintervals for the position
        num_bins_velocity = 8 # 8 subintervals for the velocity
        self.bins_position = np.linspace(-1.2, 0.6, num_bins_position + 1)
        self.bins_velocity = np.linspace(-0.07, 0.07, num_bins_velocity + 1)
        
        self.Q = np.zeros((num_bins_position, num_bins_velocity, 3)) # Q[position, velocity, action]
        
        self.greedy = False
        
        
    def _discretize(self, state):
        state_position = np.digitize(state[0], self.bins_position) - 1
        state_velocity = np.digitize(state[1], self.bins_velocity) - 1
        return (state_position, state_velocity)
    
    
    def act(self, state):
        current_state = self._discretize(state)
        
        if not self.greedy and np.random.random() < self.epsilon:
            chosen_action = self.action_space.sample()
        
        else:
            chosen_action = np.argmax(self.Q[current_state[0], current_state[1], :])
            
        return chosen_action
        
        
    def train(self, state, action, reward, next_state, terminated):
        state, next_state = self._discretize(state), self._discretize(next_state)
        
        if not terminated:
            rest_of_the_episode_estimation = np.max(self.Q[next_state[0], next_state[1], :])
        else:
            rest_of_the_episode_estimation = 0.
        
        self.Q[state[0], state[1], action] += \
            self.alpha * (reward + self.gamma * rest_of_the_episode_estimation - self.Q[state[0], state[1], action])
    

env = gymnasium.make("MountainCar-v0")
agent = QAgent(env.action_space)

# Training
print("Training the agent...")
agent.greedy = False

total_returns = []
for _ in range(1000):
    state, _ = env.reset()
    done = False
    R = 0. # return
    
    while not done:
        action = agent.act(state)
        next_state, reward, terminated, truncated, _ = env.step(action)
        agent.train(state, action, reward, next_state, terminated)
        state = next_state
        done = terminated or truncated
        R += reward
        
    total_returns.append(R)

env.close()

plt.plot(utils.moving_average(total_returns, 10))
plt.show()

# Evaluation
print("Evaluating the trained agent...")
agent.greedy = True
print("Obtained returns:", utils.simulate(agent, "MountainCar-v0", steps=200, episodes=3))
