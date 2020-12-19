import pygame


pygame.init()
win = pygame.display.set_mode((500, 490))
pygame.display.set_caption("Tileks' game")
programIcon = pygame.image.load('game\ikon.png')
pygame.display.set_icon(programIcon)



walkRight = [pygame.image.load('game\pygame_right_1.png'),
             pygame.image.load('game\pygame_right_2.png'),
             pygame.image.load('game\pygame_right_3.png'),
             pygame.image.load('game\pygame_right_4.png'),
             pygame.image.load('game\pygame_right_5.png'),
             pygame.image.load('game\pygame_right_6.png')]
walkLeft = [pygame.image.load('game\pygame_left_1.png'),
            pygame.image.load('game\pygame_left_2.png'),
            pygame.image.load('game\pygame_left_3.png'),
            pygame.image.load('game\pygame_left_4.png'),
            pygame.image.load('game\pygame_left_5.png'),
            pygame.image.load('game\pygame_left_6.png')]
playerStand = pygame.image.load('game\pygame_idle.png')
bg = pygame.image.load('game\pygame_bg.jpg')
clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')
pygame.mixer.music.load('bgmusic.mp3')
pygame.mixer.music.play(-1)

score = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 10, self.y, 38, 70)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 10, self.y, 38, 70)
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 420
        self.walkCount = 0
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render('-10', True, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class snaryad(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('game\R1E.png'),
                 pygame.image.load('game\R2E.png'),
                 pygame.image.load('game\R3E.png'),
                 pygame.image.load('game\R4E.png'),
                 pygame.image.load('game\R5E.png'),
                 pygame.image.load('game\R6E.png'),
                 pygame.image.load('game\R7E.png'),
                 pygame.image.load('game\R8E.png'),
                 pygame.image.load('game\R9E.png'),
                 pygame.image.load('game\R10E.png'),
                 pygame.image.load('game\R11E.png')]
    walkLeft = [pygame.image.load('game\L1E.png'),
                pygame.image.load('game\L2E.png'),
                pygame.image.load('game\L3E.png'),
                pygame.image.load('game\L4E.png'),
                pygame.image.load('game\L5E.png'),
                pygame.image.load('game\L6E.png'),
                pygame.image.load('game\L7E.png'),
                pygame.image.load('game\L8E.png'),
                pygame.image.load('game\L9E.png'),
                pygame.image.load('game\L10E.png'),
                pygame.image.load('game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 10
        self.hitbox = (self.x + 17, self.y, 35, 60)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0],
                                                self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 20,
                              50 - (5 * (9 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y, 35, 60)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        '''if self.health > 0:
            self.health -= 1
        else:
            self.visible = False'''
        print("hit")


def drawWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), True, (0, 0, 0))
    win.blit(text, (365, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True, True)
man = player(200, 420, 60, 75)
goblin = enemy(-30, 434, 64, 64, 440)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    #if goblin.visible == True:
    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and \
            man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and \
                man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()
            score -= 10

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and \
                bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and \
                    bullet.x - bullet.radius\
                    < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(snaryad(round(man.x + man.width // 2),
                                   round(man.y + man.height // 2),
                                   6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    drawWindow()

    pygame.display.update()
pygame.quit()
