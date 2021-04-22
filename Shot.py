import pygame

class Shot:

    def __init__(self, pLoc, pVect, pVelocity, pSize):
        self.maincolor = pygame.Color(30, 30, 30)
        self.loc = pLoc
        self.vect = pVect
        self.velocity = pVelocity
        self.size = pSize

    def setVector(self, pVect):
        # check if actual list and correct size
        self.vect = pVect
    
    def setSpeed(self, pVel):
        self.velocity = pVel
    
    def setLocation(self, pLoc):
        # check if actual list and correct size
        self.loc = pLoc

    def setSize(self, pSize):
        # right now simple one parameter size setting
        self.size = pSize

    def draw(self, pSurface):
        pygame.draw.circle(pSurface, self.maincolor, [self.loc[0], self.loc[1]], self.size, 4) #surface, color, center, radius, width
    
    def updateLocation(self):
        self.loc[0] = self.loc[0] + self.velocity * self.vect[0]
        self.loc[1] = self.loc[1] + self.velocity * self.vect[1]
