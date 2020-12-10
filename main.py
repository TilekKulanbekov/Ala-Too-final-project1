import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Tileks' game")

walkRight = [pygame.image.load('tramp/right_1.png'),
pygame.image.load('tramp/right_2.png'), pygame.image.load('tramp/right_3.png'),
pygame.image.load('tramp/right_4.png'), pygame.image.load('tramp/right_5.png'),
pygame.image.load('tramp/right_6.png')]

walkLeft = [pygame.image.load('tramp/left_1.png'),
pygame.image.load('tramp/left_1.png'), pygame.image.load('tramp/left_1.png'),
pygame.image.load('tramp/left_1.png'), pygame.image.load('tramp/left_1.png'),
pygame.image.load('tramp/left_1.png')]

bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False
JumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():

    global animCount

    if animCount + 1 >=30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x,y))

    win.blit(bg, (0, 0))
    pygame.display.update()

run = True
while run:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount **2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10

    drawWindow()

    win.fill((0,0,0))


    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update()
pygame.quit()
