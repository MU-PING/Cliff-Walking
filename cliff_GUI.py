import pygame

class Cliff_GUI():
    
    def __init__(self, win_H, win_W):
        
        #initialize pygame modules   
        pygame.init() 
        
        # initialize Clock
        self.clock= pygame.time.Clock() 
        
        # display game window
        self.UNIT = 40
        self.size_H = win_H * self.UNIT
        self.size_W = win_W * self.UNIT
    
        # create the display surface object of specific dimension.
        self.display = pygame.display.set_mode((self.size_W, self.size_H))
        
        # color
        self.ground_color = (255, 255, 255)
        self.cliff_color = (0, 0, 0)
        self.S_color = (255, 0, 0)
        self.G_color = (255, 255, 0)
  
        
    def drawFrame(self, frames, type_, run, episode):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frames.crashed = True
                
        # draw caption
        pygame.display.set_caption("Cliff Walking ("+ type_ + ")" + " Run: " + str(run) + " Episode: " + str(episode))
        
        # draw background
        pygame.draw.rect(self.display, self.ground_color, pygame.Rect(0, 0, self.size_W, self.size_H))
        
        # draw grid
        for x in range(0, self.size_W, self.UNIT):
            for y in range(0, self.size_H, self.UNIT):
                pygame.draw.rect(self.display, (200, 200, 200), pygame.Rect(x, y, self.UNIT, self.UNIT), 1)
                
        # draw cliff
        for cliff in frames.cliffs:
            pygame.draw.rect(self.display, self.cliff_color, pygame.Rect(cliff[1]*self.UNIT+4, cliff[0]*self.UNIT+4, self.UNIT-8, self.UNIT-8)) 
            
        # draw G
        pygame.draw.rect(self.display, self.G_color, pygame.Rect(frames.G[1]*self.UNIT+4, frames.G[0]*self.UNIT+4, self.UNIT-8, self.UNIT-8))
        
        # draw S
        pygame.draw.rect(self.display, self.S_color, pygame.Rect(frames.S[1]*self.UNIT+4, frames.S[0]*self.UNIT+4, self.UNIT-8, self.UNIT-8))
        
        # update pygame
        pygame.display.update()
        
        self.clock.tick(10000)
        
    def quit_(self):
        pygame.quit()