class Frames():
    
    def __init__(self, win_H, win_W):
        self.win_H = win_H
        self.S_ = [win_H-1, 0]
        self.G = [win_H-1, win_W-1]
        
        # init cliff
        self.cliffs = []
        for i in range(1, win_W-1):
            self.cliffs.append([win_H-1, i])
        
        self.crashed = False
    
    def reset(self):
        self.S = [self.win_H-1, 0]
        
class Cliff_env():
    
    def __init__(self, win_H, win_W):
        self.win_H = win_H   # grid height
        self.win_W = win_W  # grid width
        self.n_actions = 4 # up down right left
        self.frame = Frames(self.win_H, self.win_W)    
        
    def reset(self):
        self.frame.reset()
        
    def step(self, action):
        if action == 0:   # up
            if self.frame.S[0] > 0:
                self.frame.S[0] -= 1
        elif action == 1:   # down
            if self.frame.S[0] < self.win_H-1:
                self.frame.S[0] += 1
        elif action == 2:   # right
            if self.frame.S[1] < self.win_W-1:
                self.frame.S[1] += 1
        elif action == 3:   # left
            if self.frame.S[1] > 0:
                self.frame.S[1] -= 1

        # reward function
        if self.frame.S == self.frame.G:
            reward = 1
            done = True
            
        elif self.frame.S in self.frame.cliffs:
            reward = -100
            done = True
            
        else:
            reward = -1
            done = False 
        
        return reward, done
