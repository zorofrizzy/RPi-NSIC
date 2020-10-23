import sys
import pygame
import time
pygame.init()


size = width,height =640,540
speed = [1,2]
black = 0,0,0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("pokeball.png")
ballrect=ball.get_rect()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT : sys.exit()


    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0] =-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]

    #screen.fill(black)
    screen.blit(ball,ballrect)
    #time.sleep(3)
    pygame.display.flip()
    #time.sleep(2)

"""
pygame.color
pygame.display
pygame.draw
pygame.event
pygame.font
pygame.image
pygame.key
pygame.rect
pygame.surface
pygame.transform
pygame.sprite"""
