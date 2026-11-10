import pygame
from pygame.locals import *

#background/screen
background = [1, 1, 2, 2, 2, 1]
screen = [0]*6             
for i in range(6):
    screen[i] = background[i] #sets screen and background values equal to each other respectively like screen[1] = background [1]
print(screen)
[1, 1, 2, 2, 2, 1]

#assigning player position at spot 3 of the list and making it "8"
playerpos = 3
screen[playerpos] = 8
print(screen)
[1, 1, 2, 8, 2, 1]

screen[playerpos] = background[playerpos] #in the code below your changing screen[playerpos] to the 3rd place in the list but the background[playerpos] is unchanged so it will create a duplicate. if you have this it will move both at the same time so no duplicates will be made
playerpos = playerpos - 1 #goes from value of 3 to 2 so when its used in screen[playerpos] it will now be at the 3rd value not the 4th
screen[playerpos] = 8 #assigns the playerpos (which is set to equal 2) a new value (8)
print(screen)
[1, 1, 8, 2, 2, 1]

#samething as before just moving it again
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)
[1, 8, 2, 2, 2, 1]