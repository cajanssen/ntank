import pygame, os, sys, Tank
from pygame.locals import *
from Tank import *
from Shot import *


print("Start of script")
print("SDL version ", pygame.get_sdl_version())

pygame.init()
fpsClock = pygame.time.Clock()  # create an instance of a clock
surface = pygame.display.set_mode((1200,900))  # create a drawing surface
backgroundColor = pygame.Color(100,149,237)  # create a blue color for use as background
redColor = pygame.Color(200, 100, 100)

mTank = Tank("MAIN")
mTank.setLocation(200, 300)
mShotList = []
mShotCount = 0
mShotMax = 5

tankSpeed = 5

while True:
    surface.fill(backgroundColor)  # blank the screen at the start of the loop
    mTank.draw(surface)  # draw tank at its current location
    mTank.calculateTurretVector(pygame.mouse.get_pos())
    for event in pygame.event.get():
        # if event.type == QUIT:  # event from closing the windows [can also do direct equality comparison]
        if event.type in (QUIT,):  # event from closing the window
            pygame.quit()  # not necessary if entire python program is shutting down
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print("fire")
            mouseLoc = pygame.mouse.get_pos()  # if mouse leaves window returns last location
            print("Mouse at: ", mouseLoc)
            print ("turret vector: ", mTank.getTurretVector())
            # add shot decay and removal, change addition from append()
            if mShotCount < mShotMax:
                mShotList.append(Shot(mTank.getTurretEnd(), mTank.getTurretVector(), 10, 5))
                mShotCount += 1
    for mShot in mShotList:
        mShot.draw(surface)
        mShot.updateLocation()

    keyboard = pygame.key.get_pressed()  # get list booleans representing state of keyboard keys
    if keyboard[pygame.K_a]:
        mTank.move(-tankSpeed, 0)
    if keyboard[pygame.K_d]:
        mTank.move(tankSpeed, 0)
    if keyboard[pygame.K_w]:
        mTank.move(0, -tankSpeed)
    if keyboard[pygame.K_s]:
        mTank.move(0, tankSpeed)

    #pygame.draw.line(surface, redColor, [100, 100], [400, 200])  # draw line, apparently takes tuples or lists
    #pygame.display.update()  # redraw part/all of the screen (swap the back buffer with the front buffer)
    pygame.display.flip()  # redraw the screen (swap the back buffer with the front buffer)
    fpsClock.tick(30) # inserts a pause so that it runs at the specified frames per second

print("End of script")  # never reached because program exits at sys.exit() inside loop


