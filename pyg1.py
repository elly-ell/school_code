import pygame
import random

# Initializze the pygame
pygame.init()

#create the screen              # width, height
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load("space.png")

# Title and Icon
pygame.display.set_caption("Space Invader") #title

icon = pygame.image.load("ufo.png") #icon
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load("player.png")
playerX = 380
playerY = 500
playerX_change = 0

# enemy
enemy_image = pygame.image.load("enemy.png")
enemyX = random.randint (0,800)
enemyY = random.randint (20, 100)
enemyX_change = 0.5
enemyY_change = 40

# bullets
# ready - you cant see the bullet on the screen
#fire - the bullet is currently moving

bullets_image = pygame.image.load("bullets.png")
bulletsX = 0
bulletsY = 500
bulletsX_change = 0
bulletsY_change = 1
bullets_state = "ready"

def player(x,y):
    screen.blit(player_image, (x, y))

def enemy(x,y):
    screen.blit(enemy_image, (x , y ))

def fire_bullets(x,y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bullets_image, (x + 16  , y + 10))

#Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            print("keystroke is pressed")
            if event.key == pygame.K_a:
                playerX_change = -0.8
                print(playerX)
            
            if event.key == pygame.K_d:
                playerX_change = 0.8
                print(playerX)

            if event.key == pygame.K_SPACE:
                if bullets_state is "ready" :
                    # get the curret x coordinate of the spaceship
                    bulletsX = playerX
                    fire_bullets (bulletsX, bulletsY)

        if event.type == pygame.KEYUP:
                print("keystore is release")
                if event.key == pygame.K_a or  event.key == pygame.K_d:
                    playerX_change = 0
                    print("keystroke has been release")        

#SCREEN/DISPLAY LAYER 
    # red, green, blue (RGB)
    screen.fill((0,0,0)) #color of the screen
    screen.blit(background, (0,0))

#boundaries   
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

#enemy movements
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY += enemyY_change 

    elif enemyX >= 736:
        enemyX_change = -0.5
        enemyY += enemyY_change
    
    #BULLET MOVEMENT
    if bulletsY <= 0:
        bulletsY = 500
        bullets_state = "ready"

    if bullets_state is "fire":
        fire_bullets(bulletsX, bulletsY)
        bulletsY -= bulletsY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update() #always updating












