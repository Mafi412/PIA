import numpy as np
import gymnasium as gym


def simulate(agent, env_name, steps=1000, episodes=1, **env_args):
    """
    Renders the behavior of the given agent in the chosen environment and returns average
    of the obtained returns.
    
    Parameters
    ----------
    agent:
        Agent which is to be visualized - must implement method
        `agent.act(observation, reward, done)`
        
    env:
        Gymnasium environment that is to be used
    
    steps: int
        Maximum number of timesteps per episode in the environment which are to be simulated
    
    episodes: int
        Number of episodes that are to be simulated - each with maximum number of timesteps `steps`.
    """
    
    env = gym.make(env_name, render_mode="human", **env_args)
    
    returns = []
        
    for _ in range(episodes):
        observation, _ = env.reset()
        agent.reset() 
        done = False
        reward, R, timestep = 0., 0., 0
        
        while not done and timestep < steps:
            action = agent.act(observation, reward, done)
            observation, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            R += reward
            timestep += 1
            
        returns.append(R)
            
    env.close()
    
    return returns
            

def moving_average(x, n):
    weights = np.ones(n)/n
    return np.convolve(np.asarray(x), weights, mode="valid")
