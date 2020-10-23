import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()         # to define the frame rate.

x = 50                              #position of object initially, begins from top left corner.
y = 400                             # same as above, (0,0) for top left.
width = 64                          # of the object we are taking
height = 64                         # of the object
vel = 5                             #speed of the object
isJump = False                      # variable to include the jump
jumpCount = 10                      #to send the character up
left = False                        #used to define whether the character is moving left or right to change the sprites.
right = False                       #same as above, used to tell if the character is facing the right side to change the sprite.
walkCount = 0                       # this is a variable with which we will treat the walk left / walk right functions as an array, we use this to index the same.


def redrawGameWindow():
    global walkCount                #defining it globally
    win.blit(bg, (0,0))             #used to set the background after the trailing is complete.

    if walkCount + 1 >= 27:         #if the walkCount is more than the fps, we give it as zero and the default image comes in or the previous image stays as is.
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))             # if LEFT IS TRUE, we increment the walk count by 1 and print the left side sprites.
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))            #if the RIGHT is TRUE, we increment the walk count by 1 and print the right side sprites in an order that each sprite remains on for exactly, 3 frames.
        walkCount +=1
    else:
        win.blit(char, (x,y))                               #else the default character value stays in.
    
    pygame.display.update()                                 #updating the display to check the movement.


#mainloop                                                   #main loop, here we set the frames, the  movement and the keys.
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():                        # loop to exit the game.
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()                         #stores the value of the key we pressed.

    if keys[pygame.K_LEFT] and x > vel:                     #on pressing the left key, such that the object is inside the frame, we shift the object by its defined velocity.
        x -= vel
        left = True                                         # setting left and right to set the sprites for each case.
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:    #for the right side, such that the object stays within bounds.
        x += vel
        right = True
        left = False
    else:
        right = False                                       # on no movement, thge previous movement to remain in place.
        left = False
        walkCount = 0
        
    if not(isJump):                                         #setting jump.
        if keys[pygame.K_SPACE]:                            #jumps on space.
            isJump = True
            right = False                                   #LEFT and RIGHT, both are set to false so that the proper jump sprite can ber accessed.
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:                                #statement defining jump, we swuare to make a parabola, thus defining a jump.
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()                                      # calling the function to refresh the screen.

pygame.quit()


