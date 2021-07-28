import pygame, os, sys, Tank
from pygame.locals import *
from Tank import *
from Shot import *
from ShotManager import *
from LevelManager import *
from Arena import *

print("Start of script")
print("SDL version ", pygame.get_sdl_version())

pygame.init()
fpsClock = pygame.time.Clock()  # create an instance of a clock
sWidth = 1400
sHeight = 900
surface = pygame.display.set_mode((sWidth,sHeight))  # create a drawing surface
backgroundColor = pygame.Color(100,149,237)  # create a blue color for use as background
redColor = pygame.Color(200, 100, 100)
fpsRate = 30  # number of action loops per second

plTank = Tank("Player")  # create player tank
plTank.setLocation(200, 300)
#shotManager = ShotManager()
plTank.getShotManager().setMainMaxCount(5)
plTank.getShotManager().setFPSRate(fpsRate)
plTank.getShotManager().setMShotDurationInSeconds(3)
plTankSpeed = 5
tankManager = TankManager()
levelManager = LevelManager(tankManager)


while True:
    surface.fill(backgroundColor)  # blank the screen at the start of the loop
    levelManager.getCurrentArena().draw(surface)  # draw arena features
    levelManager.getTankManager().drawTanks(surface)
    plTank.draw(surface)  # draw player tank at its current location
    plTank.calculateTurretVector(pygame.mouse.get_pos())
    for event in pygame.event.get():
        # if event.type == QUIT:  # event from closing the windows [can also do direct equality comparison]
        if event.type in (QUIT,):  # event from closing the window
            pygame.quit()  # not necessary if entire python program is shutting down
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #print("fire")
            mouseLoc = pygame.mouse.get_pos()  # if mouse leaves window returns last location
            #print("Mouse at: ", mouseLoc)
            #print ("turret vector: ", plTank.getTurretVector())            
            plTank.getShotManager().requestMShot(plTank.getTurretEnd(), plTank.getTurretVector())

    plTank.getShotManager().drawShots(surface)
    plTank.getShotManager().updateShots()  # mainly update new show locations based on each speed and direction
    plTank.getShotManager().checkCollisions(levelManager.getTankManager().getTankList())  # check collisions between shots and tank list
    plTank.getShotManager().checkArenaContact(levelManager.getCurrentArena().getWallBlocks(), sWidth, sHeight)  # check for shots encountering walls
    # shot behavior when ecountering walls currently handled in ShotManager


    keyboard = pygame.key.get_pressed()  # get list booleans representing state of keyboard keys
    # before executing each directional move, check to see if encountering any 
    #    wall pieces in the direction moving
    # downside of this binary check - might stop up to plTankSpeed pixels away from wall
    #    could correct this by having the response from the check to indicate how many more
    #    pixels can move in the given direction and have the move adjust accordingly
    if keyboard[pygame.K_a]:
        if plTank.checkArenaClearXMinus(levelManager.getCurrentArena(), sWidth, sHeight):
            plTank.move(-plTankSpeed, 0)
    if keyboard[pygame.K_d]:
        if plTank.checkArenaClearXPlus(levelManager.getCurrentArena(), sWidth, sHeight):
            plTank.move(plTankSpeed, 0)
    if keyboard[pygame.K_w]:
        if plTank.checkArenaClearYMinus(levelManager.getCurrentArena(), sWidth, sHeight):
            plTank.move(0, -plTankSpeed)
    if keyboard[pygame.K_s]:
        if plTank.checkArenaClearYPlus(levelManager.getCurrentArena(), sWidth, sHeight):
            plTank.move(0, plTankSpeed)



    #pygame.draw.line(surface, redColor, [100, 100], [400, 200])  # draw line, apparently takes tuples or lists
    #pygame.display.update()  # redraw part/all of the screen (swap the back buffer with the front buffer)
    pygame.display.flip()  # redraw the screen (swap the back buffer with the front buffer)
    fpsClock.tick(fpsRate) # inserts a pause so that it runs at the specified frames per second

print("End of script")  # never reached because program exits at sys.exit() inside loop


