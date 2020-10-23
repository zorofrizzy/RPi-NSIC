import pygame
import time
pygame.init()
width = 500
height = 600
size = width,height =500,600
screen = pygame.display.set_mode(size)
black = (0,0,0)
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
screen.fill(black)
pygame.draw.rect(screen, (227,11,93),[75,10,50,20],0)
pygame.display.flip()
time.delay(10)


pygame.quit()
