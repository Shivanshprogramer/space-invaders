# set up player
px = 0
player = Rect(600, 600, 100, 100)

# set up Invaders
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
        if e.type = QUIT :
            gameOver = True
        elif e.type == KEYDOWN:
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
            dx = moveAliens(invaderList, dx)
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
                enemyBullets.append(Rect(i,x,i,y,5,20))
                
            # move enemy bullets and check collision with player
        for b in enemyBullets:
            b.move_ip(0,3)
            if b.colliderect(player):
                gameOver = True
            if b.y > height :
                enemyBullets.remove(b)
                
         
        
        
        # draw the screen 
        screen.fill((0,0,0))
        
        # draw invaders
        
        drawInvaders(invaderList, screen)
        
        # drawPlayer
        screen.blit(playerImage, player)
        
        #draw bullets
        for b in playerBullets:
            draw.rect(screen, (255,255,255), b)
            for b in enemyBullets:
                draw.rect(screen, (255,0,0), b)
                
        # show the newly drawn screen (double buffering)
        display.flip()
        
        # short delay to slow down animation
        
        time.delay(5)
                
                
            
            
        
        
            

