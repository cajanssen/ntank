import pygame, os, sys, Tank
from pygame.locals import *
from Tank import *


print("Start of script")
print("SDL version ", pygame.get_sdl_version())

pygame.init()
fpsClock = pygame.time.Clock()  # create an instance of a clock
surface = pygame.display.set_mode((800,600))  # create a drawing surface
backgroundColor = pygame.Color(100,149,237)  # create a blue color for use as background
redColor = pygame.Color(200, 100, 100)

mtank = Tank("MAIN")
mtank.setLocation(200, 300)

while True:
    surface.fill(backgroundColor)  # blank the screen at the start of the loop
    mtank.draw(surface)  # draw tank at its current location
    for event in pygame.event.get():
        # if event.type == QUIT:  # event from closing the windows [can also do direct equality comparison]
        if event.type in (QUIT,):  # event from closing the window
            pygame.quit()  # not necessary if entire python program is shutting down
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print("fire")
    keyboard = pygame.key.get_pressed()  # get list booleans representing state of keyboard keys
    if keyboard[pygame.K_a]:
        mtank.move(-2, 0)
    if keyboard[pygame.K_d]:
        mtank.move(2, 0)
    if keyboard[pygame.K_w]:
        mtank.move(0, -2)
    if keyboard[pygame.K_s]:
        mtank.move(0, 2)

    #pygame.draw.line(surface, redColor, [100, 100], [400, 200])  # draw line, apparently takes tuples or lists
    #pygame.display.update()  # redraw part/all of the screen (swap the back buffer with the front buffer)
    pygame.display.flip()  # redraw the screen (swap the back buffer with the front buffer)
    fpsClock.tick(30)

print("End of script")  # never reached because program exits at sys.exit() inside loop


