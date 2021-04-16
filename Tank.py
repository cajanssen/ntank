import pygame

class Tank:
    def __init__(self, name):
        self.name = name
        self.maincolor = pygame.Color(30, 30, 30)
        print("created tank named = " , self.name)
        self.xloc = 0
        self.yloc = 0

    def draw(self, psurface):
        #pygame.draw.line(psurface, self.maincolor, [px, py], [px + 200, py + 200], 4)
        pygame.draw.circle(psurface, self.maincolor, [self.xloc, self.yloc], 50, 4)

    def setLocation(self, px, py):
        self.xloc = px
        self.yloc = py
    
    def move(self, px, py):
        self.xloc = self.xloc + px
        self.yloc = self.yloc + py
