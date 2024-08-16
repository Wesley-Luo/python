import pygame
import random
import time
import os

pygame.init()
pygame.display.set_caption("貪食蛇")
SCRN_W = 1000
SCRN_H = 600
FPS = 60
screen = pygame.display.set_mode((SCRN_W,SCRN_H))
clock = pygame.time.Clock()
font_name = os.path.join("greedy snake","font.ttf")
snake_img = pygame.transform.scale(pygame.image.load(os.path.join("greedy snake","snake.png")),(60,60))
body_img = pygame.transform.scale(pygame.image.load(os.path.join("greedy snake","snake_body.png")),(30,30))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("greedy snake","snake_backdrop.png")),(1000,600))
starting_img = pygame.image.load(os.path.join("greedy snake","snake_starting_img.png"))

food_imgs = [pygame.image.load(os.path.join("greedy snake","apple.png")),pygame.image.load(os.path.join("greedy snake","bananas.png")),
pygame.image.load(os.path.join("greedy snake","donut.png")),pygame.image.load(os.path.join("greedy snake","orange.png")),pygame.image.load(os.path.join("greedy snake","taco.png")),
pygame.image.load(os.path.join("greedy snake","watermelon.png")),pygame.image.load(os.path.join("greedy snake","strawberry.png"))]
for i in range(len(food_imgs)):
    food_imgs[i] = pygame.transform.scale(food_imgs[i],(40,40))
    if i == 6:
        food_imgs[i] = pygame.transform.scale(food_imgs[i],(30,50))

ouch_sd = pygame.mixer.Sound(os.path.join("greedy snake","snake_ouch.wav"))
eat_sd = pygame.mixer.Sound(os.path.join("greedy snake","bite.wav"))
win_sd = pygame.mixer.Sound(os.path.join("greedy snake", "win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("greedy snake", "lose.wav"))
pygame.mixer.music.load(os.path.join("greedy snake","garden.wav"))
long = 10
bx = 0
by = 0
px = 0
py = 0
tmr = 0

snake_speed = 5
move = [0,-1,180]
pygame.display.set_icon(snake_img)

def draw_text(surf,text, size, x, y,col):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def check_pos():
    if tmr%snake_speed == 0:
        global bx,by
        bx = snake.rect.centerx
        by = snake.rect.centery

def win():
    screen.blit(back_img,(0,0))
    draw_text(screen,"You win!",200,SCRN_W/2,150,"green")
    pygame.display.flip()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit() 

def lose():
    screen.blit(back_img,(0,0))
    draw_text(screen,"You lose!",200,SCRN_W/2,150,"red")
    pygame.display.flip()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = snake_img
        self.rect = self.image.get_rect()
        self.rect.x = SCRN_W/2
        self.rect.y = SCRN_H/2
        self.point = (self.rect.centerx,self.rect.centery)
        self.tongue = 20
    def update(self):
        self.image = pygame.transform.rotate(snake_img,move[2])
        self.rect.x += move[0]*snake_speed
        self.rect.y += move[1]*snake_speed

        if move == [0,-1,180]:
            px = self.rect.centerx
            py = self.rect.centery - self.tongue
        if move == [0,1,0]:  
            px = self.rect.centerx
            py = self.rect.centery + self.tongue
        if move == [-1,0,-90]:
            px = self.rect.centerx - self.tongue
            py = self.rect.centery
        if move == [1,0,90]:
            px = self.rect.centerx + self.tongue
            py = self.rect.centery
        self.point = (px,py)

        if self.rect.y <= -50:
            self.rect.y = SCRN_H-1
        if self.rect.y >= SCRN_H:
            self.rect.y = -50
        if self.rect.x <= -50:
            self.rect.x = SCRN_W-1
        if self.rect.x >= SCRN_W:
            self.rect.x = -50

class Body(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotate(body_img,move[2])
        self.rect = self.image.get_rect()
        self.rect.centerx = bx
        self.rect.centery = by
        self.tmr = 0
    def update(self):
        global long
        snake_new_img = pygame.transform.rotate(snake_img,move[2])
        screen.blit(snake_new_img,(snake.rect.x,snake.rect.y))
        self.tmr += 1
        if self.tmr >= long:
            self.rect.y = 1000
            bodysp.remove(self)
            allsp.remove(self)

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = food_imgs[random.randint(0,6)]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50,950)
        self.rect.centery = random.randint(50,550)
    def update(self):
        global move
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] == 1 and move != [0,1,0]:
            move = [0,-1,180]
        if key[pygame.K_DOWN] == 1 and move != [0,-1,180]:
            move = [0,1,0]
        if key[pygame.K_LEFT] == 1 and move != [1,0,90]:
            move = [-1,0,-90]
        if key[pygame.K_RIGHT] == 1 and move != [-1,0,-90]:
            move = [1,0,90]

        screen.blit(self.image,(self.rect.centerx,self.rect.centery))

allsp = pygame.sprite.Group()
bodysp = pygame.sprite.Group()
snakesp = pygame.sprite.Group()
fruitsp = pygame.sprite.Group()
snake = Snake()
body = Body()
fruit = Fruit()
allsp.add(body)
bodysp.add(body)
allsp.add(snake)
snakesp.add(snake)

for i in range(3):
    fruit = Fruit()
    fruitsp.add(fruit)

pygame.mixer.music.play(-1)

start_img = pygame.transform.scale(starting_img, (1200,900))
screen.blit(start_img, (-110,-160))
pygame.display.update()
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            waiting = False

running = True
while running:
    tmr += 1
    tmr = tmr%51

    for i in bodysp:
        if i.rect.collidepoint(snake.point):
            ouch_sd.play()
            time.sleep(1)
            lose()

    for i in fruitsp:
        if snake.rect.colliderect(i.rect):
            eat_sd.play()
            i.__init__()
            long += 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(back_img,(0,0))
    check_pos()
    body = Body()
    allsp.add(body)
    bodysp.add(body)
    allsp.update()
    allsp.draw(screen)
    snakesp.draw(screen)
    fruitsp.update()
    draw_text(screen,"score: " + str(int((long-10)/10)), 30, SCRN_W/2, 0,"red")
    pygame.display.flip()
    clock.tick(FPS)

    if (long-10)/10 >= 50:
        time.sleep(1)
        win()

pygame.quit()