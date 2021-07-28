import pygame
from Shot import *

class ShotManager:

    def __init__(self):
        self.mCount = 0
        self.mMaxCount = 0  # maximum number of shots alive at one time
        self.mList = []  # list of all shots managed by this manager
        self.mMaxDuration = 0  # life of shot in seconds, currently the same for all shots
        self.fpsRate = 1  # frames per second, used to multiply with duration of find lifetime in iterations
        self.mSpeed = 10
        self.mSize = 5
        
    def drawShots(self, pSurface):
        for mShot in self.mList:
            mShot.draw(pSurface)
    
    
    def updateShots(self):
        deleteList = []
        for mShot in self.mList:
            mShot.updateLocation()
            mShot.updateDuration()
            if mShot.getRemainingDuration() <= 0:
                deleteList.append(mShot)  # if shot expired, add to delete list
        # not the best way to do this, better to delete along the way.  However, python doesn't seem
        # to have a list object that can delete from while iterating
        for dShot in deleteList:  # after all updates, go through deleteList to remove from main list
            self.mList.remove(dShot)
            self.mCount -= 1  # reduce the tally of the total number of shots active

    def setMShotDurationInSeconds(self, pDuration):
        self.mMaxDuration = pDuration * self.fpsRate
    
    def setFPSRate(self, pRate):
        self.fpsRate = pRate

    def requestMShot(self, pLoc, pVect):
        # add shot decay and removal, change addition from append()
        if self.mCount < self.mMaxCount:
            self.mList.append(Shot(pLoc, pVect, self.mSpeed, self.mSize, self.mMaxDuration))
            self.mCount += 1
            
    def setMainMaxCount(self, pMax):
        self.mMaxCount = pMax
        
    def checkCollisions(self, pForeignList):
        # loop through shots and check for contact with foreign objects
        # right now assume list is tanks and only care about tank collisions
        # later add collisions with other objects, like other shots
        # will need to add check to ensure what the objects in the list are
        stupidplaceholder = 1
        pDeleteList = []
        sDeleteList = []

        for mShot in self.mList:
            for pTank in pForeignList:
                if ((mShot.getXLoc() >= (pTank.getXLoc() - pTank.getRadius())) and
                (mShot.getXLoc() <= (pTank.getXLoc() + pTank.getRadius())) and
               (mShot.getYLoc() >= (pTank.getYLoc() - pTank.getRadius())) and
                (mShot.getYLoc() <= (pTank.getYLoc() + pTank.getRadius()))):
                    pDeleteList.append(pTank)
                    sDeleteList.append(mShot)

        for dShot in sDeleteList:
            self.mList.remove(dShot)
            self.mCount -= 1  # reduce the tally of the total number of shots active
        for dTank in pDeleteList:
            pForeignList.remove(dTank)

    def checkArenaContact(self, pWallBlocks, pWidth, pHeight):
        deleteList = []
        # loop through shot and check for contact with arena walls and structures
        # shots are small enough that can just use the center
        for mShot in self.mList:
            # check display boundaries (exterior walls)
            # current behavior is shot ends with contact with wall, could have bounce as option later
            # current screen dimension are numbers, change to parameter or structure describing current arena (not global)
            if (mShot.getXLoc() <= 0) or (mShot.getXLoc() >= pWidth) or (mShot.getYLoc() <= 0) or (mShot.getYLoc() >= pHeight):
                deleteList.append(mShot)
            # wall blocks should be pygame.Rect's            
            for wall in pWallBlocks:
                if (((mShot.getXLoc() >= wall.left) and (mShot.getXLoc() <= wall.right) and
                (mShot.getYLoc() >= wall.top) and (mShot.getYLoc() <= wall.bottom)) and
                (not(mShot in deleteList))):
                    deleteList.append(mShot)                    
        for dShot in deleteList:  # after all updates, go through deleteList to remove from main list
            self.mList.remove(dShot)
            self.mCount -= 1  # reduce the tally of the total number of shots active
