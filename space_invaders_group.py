from pygame import *

init()

width = 1200
height = 1000

screen = display.set_mode((width, height))

invaderImage = image.load('Webp.net-resizeimage.jpg')

gameOver = False

#input - none
#output - a list of invaders

def setUpInvaders():
    invaderList = []
    
    y = 50
    num_rows = 5
    num_invaders_per_row = 10
    
    while y<= 50*num_rows:
        x = 50
        while x <= 50*num_invaders_per_row:
            invaderList.append(Rect(x,y,50,50))
            x = x + 50
            
        y = y + 50
        
    return invaderList

#input - the screen to draw on the list of invaders

#output - invaders drwan on the screen

def drawInvaders(invaderList, screen):
    for i in invaderList:
        screen.blit(invaderImage, i)


    
# set up invaders
invaderList = setUpInvaders()

while not gameOver :
    for e in event.get():
        if e.type == QUIT :
            gameOver = True
            
    screen.fill((0,0,0))
    
    #draw invaders
    drawInvaders(invaderList, screen)
    
    #show the newly drawn screen (double buffering)
    display.flip()
    
    #short delay to slow down animation
    time.delay(5)