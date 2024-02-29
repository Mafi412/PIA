import numpy as np
import gymnasium as gym


def simulate(agent, env_name, steps=1000, episodes=1, **env_args):
    """ Pomocna funkce, ktera zobrazuje chovani zvoleneho agenta v danem 
    prostredi a vrací průměr získaných returnů.
    
    Parameters
    ----------
    agent: 
        Agent, který se má vizualizovat, musí implementovat metodu
        `agent.act(observation, reward, done)`
        
    env:
        Gymnasium prostředí, které se má použít
    
    steps: int
        Maximální počet kroků v prostředí na episodu, které se mají simulovat
    
    episodes: int
        Počet episod, které se mají simulovat - každá s maximálním počtem kroků `steps`.
        
    is_jupyter: bool
        Je funkce využívána v jupyter notebooku? Pokud je nastaveno na True,
        vyžaduje následující nastavení prostředí (`env`): render_mode="rgb_array"
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
    return np.convolve(np.asarray(x), weights, mode='valid')
