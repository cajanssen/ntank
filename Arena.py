import pygame

# arena is currently a series of blocks that represent
#    walls and other solid structures
class Arena:

    def __init__(self):
        self.wallBlocks = []
        self.maincolor = pygame.Color(100,100,100)
    
    def addWallBlock(self, pRect):
        # pRect parameter is expected to be a pygame Rect
        self.wallBlocks.append(pRect)

    def draw(self, pSurface):
        for wBlock in self.wallBlocks:
            pSurface.fill(self.maincolor, wBlock)
    
    def getWallBlocks(self):
        return self.wallBlocks
        