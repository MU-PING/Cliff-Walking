import numpy as np

class RL():
    def __init__(self, win_H, win_W, n_actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.n_actions = n_actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = np.zeros([win_H, win_W, n_actions])


    def choose_action(self, observation):
        # action selection
        if (np.random.rand() < self.epsilon):
            
            # choose best action
            state_action = self.q_table[observation[0], observation[1], :]

            # some actions may have the same value, randomly choose on in these actions
            action = np.random.choice(np.argwhere(state_action == np.amax(state_action)).flatten())
            
        else:

            # choose random action
            action = np.random.randint(0, self.n_actions)
            
        return action
    
    def learn(self, *args):
        pass

# off-policy
class QLearningTable(RL):
    def __init__(self, win_H, win_W, n_actions, learning_rate=0.1, reward_decay=0.9, e_greedy=0.9):
        super().__init__(win_H, win_W, n_actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_):

        q_predict = self.q_table[s[0], s[1], a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table[s_[0], s_[1], :].max()  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table[s[0], s[1], a] += self.lr * (q_target - q_predict)  # update


# on-policy
class SarsaTable(RL):

    def __init__(self, win_H, win_W, n_actions, learning_rate=0.1, reward_decay=0.9, e_greedy=0.9):
        super().__init__(win_H, win_W, n_actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_, a_):
        q_predict = self.q_table[s[0], s[1], a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table[s_[0], s_[1], a_]  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table[s[0], s[1], a] += self.lr * (q_target - q_predict)  # update