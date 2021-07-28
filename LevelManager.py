from Arena import *
from TankManager import *


# when there are multiple levels, this will have lists of
#    all the level features
# current just a list of arenas

class LevelManager:

    def __init__(self, pTankManager):
        self.currentLevel = 1
        self.arenas = []
        self.tankManger = pTankManager
        # initially just single level/arena
        # add a more formalized arena construction area
        self.arenas.append(Arena())
        # Rect parameters - left, top, width, height
        self.arenas[0].addWallBlock(pygame.Rect(200, 0, 50, 200))
        self.arenas[0].addWallBlock(pygame.Rect(0, 350, 500, 50))
        self.arenas[0].addWallBlock(pygame.Rect(300, 650, 250, 100))
        self.arenas[0].addWallBlock(pygame.Rect(700, 150, 200, 50))
        self.arenas[0].addWallBlock(pygame.Rect(850, 200, 50, 450))
        self.arenas[0].addWallBlock(pygame.Rect(700, 650, 200, 50))
        self.arenas[0].addWallBlock(pygame.Rect(850, 800, 50, 100))

        #add a more formalized tank construction area
        tank = self.tankManger.requestTank("Comp1", 1000, 100)
        tank.setColor(50, 150, 50)
        tank.setTurretVector(0, 1.0)
        tank = self.tankManger.requestTank("Comp2", 1100, 200)
        tank.setColor(50, 50, 150)
        tank.setTurretVector(0, 1.0)
        tank = self.tankManger.requestTank("Comp3", 1150, 300)
        tank.setColor(150, 50, 50)
        tank.setTurretVector(0, 1.0)

    def getCurrentArena(self):
        return self.arenas[0]  # working with just one level/arena for now

    def getTankManager(self):
        return self.tankManger

