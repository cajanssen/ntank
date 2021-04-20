import pygame, math

class Tank:

    # currently tank stores its own location

    def __init__(self, name):
        self.name = name
        self.maincolor = pygame.Color(30, 30, 30)
        print("created tank named = " , self.name)
        self.xloc = 0
        self.yloc = 0
        self.xvec = 0
        self.yvec = 0
        self.turretEndx = 0
        self.turretEndy = 0
        
        self.tradius = 50

    def draw(self, psurface):
        #pygame.draw.line(psurface, self.maincolor, [px, py], [px + 200, py + 200], 4)
        pygame.draw.circle(psurface, self.maincolor, [self.xloc, self.yloc], self.tradius, 4) #surface, color, center, radius, width
        # simple turret
        pygame.draw.line(psurface, self.maincolor, [self.xloc, self.yloc], [(self.xloc + (self.xvec * self.tradius)), (self.yloc + (self.yvec * self.tradius))], 4)

    def setLocation(self, px, py):
        self.xloc = px
        self.yloc = py
    
    def move(self, px, py):
        self.xloc = self.xloc + px
        self.yloc = self.yloc + py

    def calculateTurretVector(self, pXYTuple):
        # should validate inputs and size of tuple
        px = pXYTuple[0]
        py = pXYTuple[1]
        # calculate a direction vector using current tank location and an external location
        zlength = math.sqrt(((px - self.xloc) ** 2.0) + ((py - self.yloc) ** 2.0))
        if zlength == 0:
            zlength = 1.0
        self.xvec = (px - self.xloc) / zlength
        self.yvec = (py - self.yloc) / zlength

    def getTurretVector(self):
        return [self.xvec, self.yvec]
    
    def getTurretEnd(self):
        return [self.turretEndx, self.turretEndy]
    
        
