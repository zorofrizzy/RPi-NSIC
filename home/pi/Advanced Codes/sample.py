import pygame
import sys
pygame.init()


width = 500
height = 600
size = (width,size)
white=[255,255,255]

screen = pygame.display.set_mode(size)
colour = [293,11,93]

k = False
screen.fill(white)
while k:
    for event in pygame.event.get():
        if pygame.event==pygame.QUIT :
            sys.exit()
            k=True
    
    pygame.draw.rect(screen, colour, [50, 200, 40, 700],0)


pygame.display.flip()
        
