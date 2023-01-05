import time
import numpy as np
import matplotlib.pyplot as plt
from cliff_env import Cliff_env
from cliff_GUI import Cliff_GUI
from RL_brain import SarsaTable, QLearningTable


def SarsaTable_update(runs, episodes):
    
    # average rewards
    rewards = np.zeros([episodes])
    
    # last run path
    path = np.zeros([env.win_H, env.win_W])
    
    for run in range(runs):
        
        RL = SarsaTable(win_H=env.win_H, win_W=env.win_W, n_actions=env.n_actions)
    
        for episode in range(episodes):
            
            # initial observation
            env.reset()
            observation = env.frame.S.copy()
            
            # RL choose action based on observation
            action = RL.choose_action(observation)
            
            total_reward = 0
            while True:
    
                # RL take action and get next observation and reward
                reward, done = env.step(action)
                observation_ = env.frame.S.copy()
                
                # draw GUI
                GUI.drawFrame(env.frame, "Sarsa", run, episode)
    
                # RL choose action based on next observation
                action_ = RL.choose_action(observation_)
                
                # RL learn from this transition (s, a, r, s, a) ==> Sarsa
                RL.learn(observation, action, reward, observation_, action_)
    
                # swap and action
                observation = observation_
                action = action_
                
                # calc total_reward
                total_reward += reward
                
                # break while loop when end of this episode
                if done: break
            
            rewards[episode] += total_reward
            
        exploitation(RL, path)
        
    return rewards , path

def QLearningTable_update(runs, episodes):
    
    # average rewards
    rewards = np.zeros([episodes])
    
    # last run path
    path = np.zeros([env.win_H, env.win_W])
    
    for run in range(runs):
    
        RL = QLearningTable(win_H=env.win_H, win_W=env.win_W, n_actions=env.n_actions)
        
        for episode in range(episodes):
                 
            # initial observation
            env.reset()
            observation = env.frame.S.copy()
    
            total_reward = 0
            while True:
                
                # RL choose action based on observation
                action = RL.choose_action(observation)
                
                # RL take action and get next observation and reward
                reward, done = env.step(action)
                observation_ = env.frame.S.copy()
                
                # draw GUI
                GUI.drawFrame(env.frame, "Q-Learning", run, episode)
                
                # RL learn from this transition (s, a, r, s) ==> QLearning
                RL.learn(observation, action, reward, observation_)
    
                # swap observation
                observation = observation_
    
                # calc total_reward
                total_reward += reward
                
                # break while loop when end of this episode
                if done:
                    break
                
            rewards[episode] += total_reward 
        
        exploitation(RL, path)
        
    return rewards, path

def exploitation(RL, path):
      
    # exploitation after learning
    env.reset()
    observation = env.frame.S.copy()
    
    while True:
        # RL choose action based on observation
        action = RL.choose_action(observation)
        
        # RL take action and get next observation and reward
        reward, done = env.step(action)
        observation_ = env.frame.S.copy()
        path[observation_[0], observation_[1]] += 1      
        
        # swap observation
        observation = observation_
        
        # break while loop when end of this episode
        if done:
            break

def experiment(runs, episodes):

    qlearn_rewards, qlearn_path = QLearningTable_update(runs, episodes)
    sarsa_rewards, sarsa_path = SarsaTable_update(runs, episodes)
    
    # experiment1-----------------------------------------------------------------
    # calc average rewards
    sarsa_rewards /= runs  
    qlearn_rewards /= runs  
    
    # moving average
    n = 3
    sarsa_avg_rewards = []
    qlearn_avg_rewards = []
    for i in range(episodes - n + 1):
        sarsa_avg_rewards.append(np.mean(sarsa_rewards[i:i+n]))
        qlearn_avg_rewards.append(np.mean(qlearn_rewards[i:i+n]))
        
    # plot result  
    plt.figure()
    plt.plot(qlearn_avg_rewards, label="Q-Learning")
    plt.plot(sarsa_avg_rewards, label="Sarsa")
    plt.title("Q-Learning v.s. Sarsa")
    plt.xlabel("Episodes")
    plt.ylabel("Sum of rewards during episode")
    plt.ylim(-120, 0)
    plt.legend()
    plt.show()
    
    # experiment2-----------------------------------------------------------------
    def draw_heapmap(title, path):
        plt.figure()
        plt.title(title)
        plt.imshow(path, cmap="Blues")
        ax = plt.gca();

        # Major ticks
        ax.set_xticks(np.arange(0, env.win_W, 1))
        ax.set_yticks(np.arange(0, env.win_H, 1))

        # Minor ticks
        ax.set_xticks(np.arange(-.5, env.win_W, 1), minor=True)
        ax.set_yticks(np.arange(-.5, env.win_H, 1), minor=True)

        # Gridlines based on minor ticks
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

        # Remove minor ticks
        ax.tick_params(which='minor', bottom=False, left=False)  
        
    draw_heapmap('Q-Learning Inference Path', qlearn_path)
    draw_heapmap('Sarsa Inference Path', sarsa_path)
    

if __name__ == "__main__":
    
    # init env & GUI
    env = Cliff_env(4, 12)
    GUI = Cliff_GUI(env.win_H, env.win_W)
    
    # experiments(runs:perform 50 independent runs, episodes:episodes of each run)
    experiment(runs = 100, episodes = 500)
    
    # close GUI
    GUI.quit_()