from pygame import *

init()

width = 1200
height = 720

screen = display.set_mode((width, height))
display.set_caption("Space Invader")

invaderImage = image.load('alien.jpg')

#colors palette
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
GOLD=( 230, 215, 0)

#invaders motion
i_move_x=1.5
i_move_y=70

#input - none
#output - a list of invaders

def setUpInvaders():
    invaderList = []
    
    y = 50
    num_rows = 4
    num_invaders_per_row = 15
    
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

gameOver = False

def play():
    global gameOver, i_move_y, i_move_x, invaderList, screen
    # set up invaders
    invaderList = setUpInvaders()
    #in case game was restarted once invaders moving in opposite dir
    if i_move_x<0:
        i_move_x*=-1

    while not gameOver :
        for e in event.get():
            if e.type == QUIT :
                gameOver = True
            elif e.type==KEYDOWN and e.key==K_ESCAPE:
                initial()

        screen.fill((0,0,0))

        for invader in invaderList:
            if invader.right > width or invader.left < 0:
                i_move_x *= -1
                for invader in invaderList:
                    invader.move_ip(0,i_move_y)
                break


        for invader in invaderList:
            invader.move_ip(i_move_x,0)

        #draw invaders
        drawInvaders(invaderList, screen)

        #show the newly drawn screen (double buffering)
        display.flip()

        #short delay to slow down animation
        time.delay(5)

def initial():

    global screen, gameOver
    screen.fill((0,0,0))
    font.init()
    myfont = font.SysFont('Comic Sans MS',26)
    textsurface = myfont.render('Enter SPACE to play the game',False,BLUE)
    screen.blit(textsurface,((width/2)-200,height-100))
    logo= image.load("logo.jpg")
    screen.blit(logo,((width/2)-200,(height/2)-200))
    display.flip()
    while not gameOver :
        for e in event.get():
            if e.type == QUIT :
                gameOver = True

            if e.type ==KEYDOWN and e.key == K_SPACE:
                play()



initial()