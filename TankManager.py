from Tank import *

class TankManager:

    def __init__(self):
        self.tCount = 0  # initialize number of tanks to zero
        self.tList = []
    
    def requestTank(self, pName, px, py):
        tank = Tank(pName)
        tank.setLocation(px, py)
        self.tList.append(tank)
        self.tCount += 1
        return tank
    
    def drawTanks(self, pSurface):
        for tank in self.tList:
            tank.draw(pSurface)
    
    def getTankList(self):
        return self.tList
