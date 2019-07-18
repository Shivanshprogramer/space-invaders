from pygame import *
import random

init()

width = 1200
height = 720

screen = display.set_mode((width, height))
display.set_caption("Space Invader")

invaderImage = image.load('alien.jpg')
lives_image= image.load('heart.jpg')
playerImage= image.load('ship.png')

#colors palette
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
GOLD=( 230, 215, 0)

#invaders motion
#exact values given inside play() function
i_move_x=0
i_move_y=0

temp_x=0
temp_y=0

paused_state=0

lives=0


player = Rect(600, 600, 100, 100)
#input - none
#output - a list of invaders

def pause():
    global paused_state,i_move_x,i_move_y,temp_x,temp_y

    if paused_state==0:
        temp_x=i_move_x
        temp_y=i_move_y
        i_move_x=0
        i_move_y=0
        paused_state=1
    elif paused_state==1:
        i_move_x=temp_x
        i_move_y=temp_y
        temp_x=0
        temp_y=0
        paused_state=0




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
    global player
    for i in invaderList:
        screen.blit(invaderImage, i)
    
    screen.blit(playerImage, player)
gameOver = False

def play():
    global gameOver, i_move_y, i_move_x, invaderList, screen, paused_state,lives, player
    # set up invaders
    invaderList = setUpInvaders()
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

    #initialising the values when game starts
    i_move_x = 1
    i_move_y = 40
    paused_state = 0
    lives = 5

    while not gameOver:
        for e in event.get():
            if e.type == QUIT:
                gameOver = True
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                initial()
            elif e.type == KEYDOWN and e.key == K_p:
                pause()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    initial() 
                if e.key == K_LEFT:
                    px = -3
                if e.key == K_RIGHT:
                    px = 3
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
                lives=lives-1
                enemyBullets.remove(b)

            if b.y > height :
                enemyBullets.remove(b)

        # drawPlayer
        screen.blit(playerImage, player)



        
        
                
        pressed= key.get_pressed()

        if pressed[K_RIGHT]==1:
            player.move_ip(2,0)
        if pressed[K_LEFT]==1:
            player.move_ip(-2,0)

        screen.fill((0,0,0))

        myfont = font.SysFont('Comic Sans MS', 18)
        textsurface = myfont.render('ESC - quit the game       P - pause the game', False, BLUE)
        screen.blit(textsurface, (30, 10))
        count=0
        while count<lives:
            screen.blit(lives_image,((width-150)+(count*30),10))
            count+=1

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

        # draw bullets
        for b in playerBullets:
            draw.rect(screen, (255, 255, 255), b)
            for b in enemyBullets:
                draw.rect(screen, (255, 0, 0), b)

        if paused_state==1:
            myfont = font.SysFont('Comic Sans MS', 60)
            textsurface = myfont.render('GAME PAUSED', False, GOLD)
            draw.rect(screen,BLACK,((width/2)-210,height/2,450,100))
            screen.blit(textsurface, ((width/2)-200, height/2))
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
