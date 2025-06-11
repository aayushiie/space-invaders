import pygame
import random
import math

from pygame import mixer

#initialise pygame (necessary)
pygame.init()

#define the size of the game screen
screen = pygame.display.set_mode((800,600)) 

#inserting a clock
clock = pygame.time.Clock()

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('play.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('bg-1.png')

#background sound
mixer.music.load("MC Hammer - U Can't Touch This (HQ).mp3")
mixer.music.play(-1)

#player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('play.png')) 
    enemyX.append(random.randint(0, 735)) 
    enemyY.append(random.randint(50, 200)) 
    enemyX_change.append(2)
    enemyY_change.append(40)

#bullet
#ready state - you can't see bullet on the screen
#fire state - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16 , y+10))

#creating a score variable
score_value = 0
font = pygame.font.Font('Minecraft.ttf', 32)
testX = 10
testY = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# game over
over_font = pygame.font.Font('Minecraft.ttf', 64)
again_font = pygame.font.Font('Minecraft.ttf', 48)
def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))
    # play_again = again_font.render("press 'f' to play again", True, (255, 255, 255))
    # screen.blit(play_again, (150, 350))
    mixer.music.stop()
    end_sound = mixer.Sound("game-over.mp3")
    end_sound.play()

#collision function
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance< 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:

    #giving background
    screen.fill((0,0,0))
    #bg image
    screen.blit(background, (0,0))
    #check each event in pygame by using the for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #when key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        #when key is released (keyup)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    
    #setting boundaries
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    #enemy movement
    for i in range(num_of_enemies):

        #game over
        # if enemyY[i] > 440:
        #     #to move all other enemies below the screen and out of screen
        #     for j in range(num_of_enemies):
        #         enemyY[j] = 2000 
        #     game_over_text()
        #     break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] -= 2
            enemyY[i] += enemyY_change[i]
        if enemyY[i] >= 460:
                enemyY[i] = random.randint(50, 200)

        #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            hit_sound = mixer.Sound("collision.mp3")
            hit_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)


    #bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    #increasing difficulty
    if score_value >= 15:
        for i in range(num_of_enemies):
            enemyX_change.append(2.5)
            enemyX[i] += enemyX_change[i]
    if score_value >= 30:
        for i in range(num_of_enemies):
            enemyX_change.append(3)
            enemyX[i] += enemyX_change[i]
            
    #calling the player on screen
    player(playerX, playerY)   

    #score 
    show_score(testX, testY)

    #display on screen
    pygame.display.update()
