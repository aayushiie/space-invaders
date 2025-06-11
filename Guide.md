# PYGAME

* [documentation](https://www.pygame.org/docs/)

## Lesson 1: Initialising

```python
    import pygame
    pygame.init()
```

---

## Lesson 2: Creating window

```python
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
```

* everything that goes on the screen is put inside the loop
* anything that we want to persist, goes inside this loop
* the update line is necessary in all games
* all events are handled inside this loop
* for loop checks each event in the pygame and if [x] button is pressed then the boolean value of 'running' is altered to break out of the loop
* closing of window is also an event
  * [ x ] button is also an event so we need to handle that inside this loop

---

## Lesson 3: Changing title, logo, background

```python
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space invader")
    icon = icon = pygame.image.load('alien-ship.png')
    pygame.display.set_icon(icon)
```

* brackets are always used to write coordinates ()

```python
    running = True
    while running:
        screen.fill((0,0,0))
```

* rgb value is entered
* screen fill is background
* every other object comes after this 'cause the screen is drawn first and on top of that other objects are drawn

---

## Lesson 4: Adding players

```python
    playerImg = pygame.image.load('space-invaders.png')
    playerX = 370
    playerY = 480

    def player():
        screen.blit(playerImg, (playerX, playerY))
    
    #calling the player
    while running:
        player()
```

* players are added in the form of function
* blit is to draw so we are drawing the player image on the screen
* blit takes two values
  * player's image
  * player's coordinates
    * coordinates will go inside bracket (x-coordinate, y-coordinate)

---

## Lesson 5: Movement mechanics

```python
    def player(x, y):
        screen.blit(playerImg, (x, y))
    
    while running:
        player(playerX, playerY)
```

* in order to be able to change the coordinates of the player, we need to send parameters so we can change them later
* we are initially passing x, y as coordinates
* later on, to set initial position on screen, we are using the initial variables: playerX, playerY
* the core idea:
  * the basic idea is that we are adding the distance we move towards right to its initial position to obtain new position and we are subtracting when we move left
  * similarly we are adding when we move down and subtracting from initial y value when we move up
* so we'll put the motion in our while loop obv so that it can happen on command or sometimes even automatically (it is an event)

```python
    running = True
    while running:
        #run any one or two different axes at a time
        playerX += 0.1  #only for testing
        playerX -= 0.1  #only for testing
        playerY += 0.1  #only for testing
        playerY -= 0.1  #only for testing
        player(playerX, playerY)
```

* as the while loop runs, the playerX values increasees by 0.1 and that value is sent to player function that goes to its definition and sets a new value of the coordinate after increment and moves the player image to that coordinate (this looks like motion)

---

## Lesson 6: Keyboard input control

```python
    playerX_change = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change -= 0.3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        player(playerX, playerY)
```

* we use the already established for loop for our events to check keyboard events as well
* we use if conditions to check events by `if event.type ==`
* KEYDOWN means that a key was pressed
* KEYUP means that a key was released
* to centralise a key, we use `if event.key ==`
* we create a new changing variable for x and y coordinates

---

## Lesson 7: Setting boundary

```python
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736: 
        playerX = 736
```

* we have our right boundary to 736 'cause the image is 64px and screen width is 800px so 800-64 = 736px. similarly other limits can be set as well

---

## Lesson 8: Creating another character i.e. our enemy

```python
    import random

    enemyImg = pygame.image.load('enemy.png')
    enemyX = random.randint(0,800)
    enemyY = random.randint(50,200)
    enemyX_change = 0

    def enemy(x, y):
        screen.blit(enemyImg, (x,y))
    
    while running:
        enemy(enemyX, enemyY)
```

* we are using random library to generate a random position for the enemy
* randint(a, b) takes two parameters that will tell the starting and ending point of random number generation i.e. the range

---

## Lesson 9: Movement Mechanics of the invader

```python
    enemyX_change = 0.3
    enemyY_change = 40

    while:
        enemyX += enemyX_change
        if enemyX <=0:
            enemyX_change = 0.3
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change -= 0.3
            enemyY += enemyY_change
        
        enemy(enemyX, enemyY)
```

* checking boundary for enemy as well using the same mechanism
* we are changing the value of '_change' variable and we are incrementing the value of original coordinate variable with the '_change' variable
* we are moving the enemy down every time it hits either of the boundary walls

---

## Lesson 10: Adding background

```python
    background = pygame.image.load('bg.png')
    while Running:
        screen.blit(background, (0,0))
```

* due to background being an additional entity of the while loop, the relative motion of other images now seems very slow so we'll increase the change from 0.3 for player and enemy to a higher value

---

## Lesson 11: Creating bullets

```python
    bulletImg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    def fire_bullet(x,y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x+16, y+10))

    while running:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_change +=5
            if event.key == pygame.K_SPACE:
                if bullet_state = "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if bulletY <=0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
```

* we got two states here:
  * ready: you can't see the bullet on the screen
  * fire: where `screen.blit()` is used to make bullets appear on the screen
* x-coordinate is set to 0 as its motion on x-axis is completely dependent on on the x-coordinate of player
  * so the x_change is also 0 or doesn't need to incorported at all
* the bullet is moving in straight line on y-axis
  * y-coordinate is initially set to 480 as that's where player is on the y-axis
* now the speed of bullet (`bulletY_change`) is set to 10
* the fire bullet function does three things
    1. makes the bullet_state global so that the changes can happen
    2. changes state from ready to fire
    3. makes the bullet visible on screen with `screen.blit()`
* the coordinates of bullet are adjusted (x, y) so that the new img starts from the top of the player (tried to make it almost center)
* inside the game loop:
    1. when space bar is pressed, we want the bullet to get fired which means its state would have to change so we call the function to do that
    2. but that alone won't do anything. we want the bullet to not only make an appearance but also show motion
    3. so we define its movement like the movement of player and enemy
    4. it will move up at bullet_change speed
* now instead of having playerX as the x-coordinate, we store the initial value of player inside our bullet's x-coordinate so that it remains stagnant with the motion of the player
* we only want the bullet to get fired when state is 'ready' hence the if condition with keystroke
* when the bullet reaches the upper end of the screen:  
  1. we don't want it to keep going after that
  2. so we change its y-coordinate back to starting position
  3. and its state back to "ready" so multiple bullets could get fired as it'd start looping due to the fire_bullet function
  4. and then we call the function again and change the the coordinates on the y-axis

---

## Lesson 12: Collision detection

* [distance calculation detail](https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint)

```python
    import math

    score = 0
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:  #estimated value (can be changed)
            return True
        else:
            return False
    
    while running:
        collision = isCollision(enemyX, enemyY, bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX = random.randint(0, 735)
            enemyY = random.randint(50, 200)
```

* distance is calculated between the x and y coordinates of bullet and that of the enemy
* the new random position is set so when an enemy is shot, it would reappear from a random spot
* the value 735 is there 'cause the position of enemy is changing inside the game loop

---

## Lesson 13: Creating multiple enemies

```python
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
    
    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x,y))

    while running:
        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] -=2
                enemyY[i] += enemyY_change[i]
            if enemyY[i] >= 460:
                enemyY[i] = random.randint(50, 200)
            
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)


```

* making the enemy attributes into lists so that it can be used later
* fixing the number of enemies at the start only
* the for loop creates each enemy and give it properties, and it appends each of these enemies values into its respective attribute's lists
* to point at the enemy, we'll use [ i ] to target it like in function enemy
* inside game loop, we'll target the each enemy using the loop
  * we are increasing the value of x coordinate (which is random due to the random module) of enemy by the `enemyX_change` value
  * we are also setting the limits like if the enemy reaches extreme left (0 on x-axis) then we'll change the `enemyX_change` value to 2 for that enemy and that'd set the `enemyX[i]` to 2 as well since (0 + 2 = 2)
  * similar thing happens with right extreme
  * we'll increase y coordinate by 40 in all cases

---

## Lesson 14: Inserting clock

```python
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
```

* to track time

---

## Lesson 15: Increasing difficulty

```python
    if score >= 15:
        for i in range(num_of_enemies):
            enemyX_change.append(2.5)
            enemyX[i] += enemyX_change[i]
    if score >= 30:
        for i in range(num_of_enemies):
            enemyX_change.append(3)
            enemyX[i] += enemyX_change[i]
```

* changing the speed at which enemies move by changing the value at which its x-coordinates get changed

---

## Lesson 16: Displaying text

```python
    score_value = 0
    font = pygame.font.Font('Minecraft.ttf', 32)
    testX = 10
    testY = 10

    def show_score(x, y):
        score = font.render("Score: " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))
    
    while running:
        show_score(testX, testY)
```

* we can download our own fonts and upload them as in the directory to use custom fonts
* we first render the text then blit it on the screen
* `font` is module and `Font` is class
* in the Font class, the second value is font size
* in font.render(), the first value is score itsefl that has to be string or in bytes, next is 'true' so that it appears on the screen, then we can specify its color and background color (in rgb)
* for the font to persist, we have to use it in our game loop

---

## Lesson 17: Adding sounds

```python
    from pygame import mixer

    mixer.music.load("filename.mp3")
    mixer.music.play(-1)

    while running:
        if collision:
            hit_sound = mixer.sound('name.mp3')
            hit_sound.play()
```

* `mixer` module has `Sounds` and `music`
* we use `mixer.Sounds` when we want the sound to play only once while for `mixer.music`, when we want the sound to play continuously under all other sounds like background music
* we use `play(-1)` play on loop

---

## Lesson 18: Ending the game

```python
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

     while running: 
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000 
            game_over_text()
            break
```

* the second loop is to move all other enemies below the screen and out of screen
