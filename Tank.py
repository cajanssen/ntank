import pygame, math
from ShotManager import *

class Tank:

    # currently tank stores its own location

    def __init__(self, name):
        self.name = name
        self.maincolor = pygame.Color(30, 30, 30)
        print("created tank named = " , self.name)
        # if change x,y coordinates for stuff to list - less parameters, but harder to verify?
        self.shotManager = ShotManager()
        self.xloc = 0
        self.yloc = 0
        self.xvec = 0
        self.yvec = 0
        self.turretEndx = 0
        self.turretEndy = 0
        
        self.tradius = 30

    # this is a very java-like way of doing this, not python-like
    # will change to a more python-like way after finding one that
    # is straight-forward
    def getShotManager(self):
        return self.shotManager

    def draw(self, pSurface):
        #pygame.draw.line(psurface, self.maincolor, [px, py], [px + 200, py + 200], 4)
        pygame.draw.circle(pSurface, self.maincolor, [self.xloc, self.yloc], self.tradius, 4) #surface, color, center, radius, width
        pygame.draw.circle(pSurface, self.maincolor, [self.xloc, self.yloc], self.tradius / 2, 2) #surface, color, center, radius, width
        # simple turret
        self.turretEndx = (self.xloc + (self.xvec * self.tradius))
        self.turretEndy = (self.yloc + (self.yvec * self.tradius))
        pygame.draw.line(pSurface, self.maincolor, [self.xloc, self.yloc], [self.turretEndx, self.turretEndy], 4)
        turretHalfx = (self.xloc + (self.xvec * self.tradius / 2))
        turretHalfy = (self.yloc + (self.yvec * self.tradius / 2))
        pygame.draw.line(pSurface, self.maincolor, [self.xloc, self.yloc], [turretHalfx, turretHalfy], 8)
        pygame.draw.line(pSurface, self.maincolor, [self.xloc + self.tradius, self.yloc - self.tradius], 
                [self.xloc + self.tradius, self.yloc + self.tradius], 4)
        pygame.draw.line(pSurface, self.maincolor, [self.xloc + self.tradius, self.yloc + self.tradius], 
                [self.xloc - self.tradius, self.yloc + self.tradius], 4)
        pygame.draw.line(pSurface, self.maincolor, [self.xloc - self.tradius, self.yloc + self.tradius], 
                [self.xloc - self.tradius, self.yloc - self.tradius], 4)
        pygame.draw.line(pSurface, self.maincolor, [self.xloc - self.tradius, self.yloc - self.tradius], 
                [self.xloc + self.tradius, self.yloc - self.tradius], 4)

    def setLocation(self, px, py):
        self.xloc = px
        self.yloc = py
    
    def setColor(self, pRed, pGreen, pBlue):
        # parameters should be integers from 0 to 255
        self.maincolor = pygame.Color(pRed, pGreen, pBlue)

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

    def setTurretVector(self, px, py):
        self.xvec = px
        self.yvec = py

    def getTurretVector(self):
        return [self.xvec, self.yvec]
    
    def getTurretEnd(self):
        return [self.turretEndx, self.turretEndy]
    
    def getXLoc(self):
        return self.xloc

    def getYLoc(self):
        return self.yloc

    def getRadius(self):
        return self.tradius

    # the following functions are to check if the tank is in contact with arena
    #    walls when moving in the four cardinal directions

    def checkArenaClearXMinus(self, pArena, pWidth, pHeight):
        returnFlag = True
        if ((self.xloc - self.tradius) <= 0):
            returnFlag = False
        # pArena should be an Arena
        wallBlocks = pArena.getWallBlocks()
        # wallBlocks should be a list of pygame.Rect
        for block in wallBlocks:
            if (((self.xloc - self.tradius) <= block.right) and
            ((self.xloc - self.tradius) >= block.left) and
            ((self.yloc + self.tradius) >= block.top) and
            ((self.yloc - self.tradius) <= block.bottom) and
            (self.xloc + self.tradius)):
                returnFlag = False
        return returnFlag
    
    def checkArenaClearXPlus(self, pArena, pWidth, pHeight):
        returnFlag = True
        if ((self.xloc + self.tradius) >= pWidth):
            returnFlag = False
        # pArena should be an Arena
        wallBlocks = pArena.getWallBlocks()
        # wallBlocks should be a list of pygame.Rect
        for block in wallBlocks:
            if (((self.xloc + self.tradius) <= block.right) and
            ((self.xloc + self.tradius) >= block.left) and
            ((self.yloc + self.tradius) >= block.top) and
            ((self.yloc - self.tradius) <= block.bottom)):
                returnFlag = False
        return returnFlag

    def checkArenaClearYMinus(self, pArena, pWidth, pHeight):
        returnFlag = True
        if ((self.yloc - self.tradius) <= 0):
            returnFlag = False
        # pArena should be an Arena
        wallBlocks = pArena.getWallBlocks()
        # wallBlocks should be a list of pygame.Rect
        for block in wallBlocks:
            if (((self.xloc - self.tradius) <= block.right) and
            ((self.xloc + self.tradius) >= block.left) and
            ((self.yloc - self.tradius) >= block.top) and
            ((self.yloc - self.tradius) <= block.bottom)):
                returnFlag = False
        return returnFlag

    def checkArenaClearYPlus(self, pArena, pWidth, pHeight):
        returnFlag = True
        if ((self.yloc + self.tradius) >= pHeight):
            returnFlag = False
        # pArena should be an Arena
        wallBlocks = pArena.getWallBlocks()
        # wallBlocks should be a list of pygame.Rect
        for block in wallBlocks:
            if (((self.xloc - self.tradius) <= block.right) and
            ((self.xloc + self.tradius) >= block.left) and
            ((self.yloc + self.tradius) >= block.top) and
            ((self.yloc + self.tradius) <= block.bottom)):
                returnFlag = False
        return returnFlag
