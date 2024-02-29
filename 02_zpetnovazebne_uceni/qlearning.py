import gymnasium
import numpy as np
import utils
import matplotlib.pyplot as plt


class QAgent:
    def __init__(self, action_space, epsilon=0.01, alpha=0.1, gamma=1.):
        self.action_space = action_space
        
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        
        self.train = True
        
        num_bins_position = 12 # 12 subintervals for the position
        num_bins_velocity = 8 # 14 subintervals for the velocity
        self.bins_position = np.linspace(-1.2, 0.6, num_bins_position + 1)
        self.bins_velocity = np.linspace(-0.07, 0.07, num_bins_velocity + 1)
        
        self.Q = np.zeros((num_bins_position, num_bins_velocity, 3)) # Q[position, velocity, action]
        self.last_state = None
        self.last_action = None
        
        
    def _discretize(self, observation):
        state_position = np.digitize(observation[0], self.bins_position) - 1
        state_velocity = np.digitize(observation[1], self.bins_velocity) - 1
        return (state_position, state_velocity)
    
    
    def act(self, observation, reward, done):
        current_state = self._discretize(observation)
        
        if self.train:
            # Training
            if self.last_state != None:
                self.Q[self.last_state[0], self.last_state[1], self.last_action] = \
                    self.alpha * (reward + self.gamma * np.max(self.Q[current_state[0], current_state[1], :])) + \
                    (1 - self.alpha) * self.Q[self.last_state[0], self.last_state[1], self.last_action]
                
            # Action selection
            if np.random.random() >= self.epsilon:
                chosen_action = np.argmax(self.Q[current_state[0], current_state[1], :])
            
            else:
                chosen_action =  self.action_space.sample()
                
            # Update of the inner memory for training
            self.last_state = current_state
            self.last_action = chosen_action
            
            return chosen_action
        
        else:
            return np.argmax(self.Q[current_state[0], current_state[1], :])
    
    
    def reset(self):
        self.last_state = None
        self.last_action = None
    

env = gymnasium.make("MountainCar-v0")

agent = QAgent(env.action_space)

# Training
agent.train = True
total_returns = []
for _ in range(1000):
    observation, _ = env.reset()
    agent.reset()
    done = False
    
    reward = 0.
    R = 0. # return
    timestep = 0
    
    while not done:
        action = agent.act(observation, reward, done)
        observation, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        R += reward
        timestep += 1
        
    total_returns.append(R)

env.close()

plt.plot(utils.moving_average(total_returns, 10))
plt.show()

# Evaluation
agent.train = False
print("Obtained returns:", utils.simulate(agent, "MountainCar-v0", steps=200, episodes=5))
