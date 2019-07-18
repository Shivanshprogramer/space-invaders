from pygame import *
import random

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
     
    
    # set up player
    px = 0
    player = Rect(600, 600, 100, 100)

    
    dx = 20
    frameCount = 0
    #set up bullets 
    playerBullets = []

    # set up enemy bullets

    enemyBullets = []
    probabilityToFire = 0.0001 # this will control how often the enemy will fire
    maxEnemyBullets = 8 # stop there being too many bullets on screen at once


    while not gameOver:
        for e in event.get():
            if e.type == QUIT:
                gameOver = True
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    initial()
                if e.key == K_LEFT:
                    px = -3
                if e.key == K_RIGHT:
                    px = 3
                if e.key == K_SPACE:
                    if len(playerBullets) < 2:
                        playerBullets.append(Rect(player.x+50, player.y,5,20))
            elif e.type == KEYUP:
                if e.key == K_LEFT or e.key == K_RIGHT:
                    px = 0 
                
        if frameCount >= 100:
            #dx = moveAliens(invaderList, dx)
            frameCount = 0
        frameCount = frameCount + 1
        # move Player
        if player.left+px < 0 or player.right+px > width : 
            px = 0
            player.move_ip(px, 0)
            
        #move bullets and check collision
        
        for b in playerBullets:
            b.move_ip(0,-3)
            if b.y < 0 :
                playerBullets.remove(b)
                for i in invaderList :
                    if i.colliderect(b):
                        invaderList.remove(i)
                        playerBullets.remove(b)
                        
        # control enemy bullets fire
        for i in invaderList:
            fireChance = random.random() # pick a number from 0 to 1
            if fireChance <= probabilityToFire  and len(enemyBullets) <= maxEnemyBullets:
                enemyBullets.append(Rect(i.x,i.y,5,20))
                
            # move enemy bullets and check collision with player
        for b in enemyBullets:
            b.move_ip(0,3)
            if b.colliderect(player):
                gameOver = True
            if b.y > height :
                enemyBullets.remove(b)
        
        # drawPlayer
        #screen.blit(playerImage, player)
        
        #draw bullets
        for b in playerBullets:
            draw.rect(screen, (255,255,255), b)
            for b in enemyBullets:
                draw.rect(screen, (255,0,0), b)
                

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