import pygame
import random
import time
import os
pygame.init()
WIDTH = 1000
HEIGHT = 600
jump = 0
f = 0
score = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("忍者大冒險")
font_name = os.path.join("ninja adventure","font.ttf")
land_img = pygame.image.load(os.path.join("ninja adventure", "grass_land.png"))
walk_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "walk.png")), (60, 60))
jump_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "jump.png")), (60, 60))
fall_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "fall.png")), (60, 60))
coin_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "ninja_coin.png")), (40, 40))
rocket_img = pygame.image.load(os.path.join("ninja adventure", "rocket.png"))
missle_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "missle.png")), (50, 100))
bomb_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "ninja_bomb.png")), (50, 50))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("ninja adventure", "ninja_back.png")),(1000,600))
starting_img = pygame.image.load(os.path.join("ninja adventure", "ninja_start_back.png"))
coin_sd = pygame.mixer.Sound(os.path.join("ninja adventure", "coin.wav"))
boom_sd = pygame.mixer.Sound(os.path.join("ninja adventure", "explode.wav"))
jump_sd = pygame.mixer.Sound(os.path.join("ninja adventure", "jump.wav"))
win_sd = pygame.mixer.Sound(os.path.join("ninja adventure", "win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("ninja adventure", "lose.wav"))
pygame.mixer.music.load(os.path.join("ninja adventure", "ninja_back_sd.wav"))
draw = 1
out = 1
land_locate = [50]  
land_pos = []
bx=0
by=0
pygame.display.set_icon(walk_img)

def draw_text(surf,text,size,x,y,col):
    global font_name
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text,True,col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_init():
    start_img = pygame.transform.scale(starting_img, (1100,800))
    screen.blit(start_img, (-60,-40))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def fill():
    global bx,by
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == 1 and ninja.rect.y <= 500:
        bx += 7
    if key[pygame.K_RIGHT] == 1 and ninja.rect.y <= 500:
        bx -= 7
    bx = bx%1000
    screen.blit(back_img,(bx,by))
    screen.blit(back_img,(bx-1000,by))

def win():
    fill()
    draw_text(screen,"You win!",200,WIDTH/2,150,"dark green")
    pygame.display.flip()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

def lose():
    fill()
    draw_text(screen,"You lose!",200,WIDTH/2,150,"red")
    pygame.display.flip()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = walk_img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT/2-50
        self.tl = 0
    def touch_land(self):
        global bx
        key = pygame.key.get_pressed()
        jump = key[pygame.K_SPACE] == 1 or key[pygame.K_UP] == 1
        if jump:
            jump_sd.play()
            self.image = jump_img
            rocketgp.update()
            for i in range(15):
                fill()
                self.rect.y -= 7
                draw_text(screen,"score: "+str(score),30,WIDTH/2,0,"black")
                all_sprites.update()
                all_sprites.draw(screen)
                coingp.update()
                bombgp.update()
                coingp.draw(screen)
                bombgp.draw(screen)
                rocketgp.draw(screen)
                misslegp.draw(screen)
                pygame.display.flip()
                pygame.display.flip()
                if key[pygame.K_LEFT] == 1:
                    for i in landgp:
                        i.right(2)
                    coin.right(2)
                    bomb.right(2)
                    rocket.left(2)
                    missle.left(2)
                if key[pygame.K_RIGHT] == 1:
                    for i in landgp:
                        i.left(2)
                    coin.left(2)
                    bomb.left(2)
                    rocket.right(2)
                    missle.left(2)
                    bx -= 2
                rocketgp.update()
                misslegp.update()
        else:
            self.image = walk_img
    def touch_coin(self):
        global score
        score += 1
        coin_sd.play()
    def touch_bomb(self):
        global boom_sd
        boom_sd.play()
        time.sleep(2)
        lose()
    def update(self):
        if self.tl == 0:
            self.rect.y += 5
            self.image = fall_img
        if self.rect.y >= 550:
            lose()

class Land(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.num = x in land_locate
        self.wid = random.randint(100, 200)
        self.image = pygame.transform.scale(land_img, (self.wid, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(100, 500)
        if self.rect.y >= 400 or self.rect.y <= 200:
            self.rect.y = 300+random.randint(-50,50)
        if f == 1 :
            self.wid = 200
            self.rect.y = 300
        land_pos.append(self.rect.y)
    def left(self,sp):
        global bx
        self.rect.x -= sp
    def right(self,sp):
        global bx
        self.rect.x += sp
    def update(self):
        global jump,bx
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == 1 and ninja.rect.y <= 500:
            self.right(7)
            bx -= 7
        if key[pygame.K_RIGHT] == 1 and ninja.rect.y <= 500:
            self.left(7)
            bx += 7

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = land_pos[len(land_pos)-1]-50
    def right(self,sp):
        self.rect.x += sp
    def left(self,sp):
        self.rect.x -= sp
    def touch_n(self):
        self.rect.x = WIDTH
        self.rect.y = land_pos[len(land_pos)-1]-50
    def update(self):
        global jump
        key = pygame.key.get_pressed()
        if self.rect.x <= -50:
            self.rect.x = WIDTH
            self.rect.y = land_pos[len(land_pos)-1]-50
        if key[pygame.K_LEFT] == 1 and ninja.rect.y <= 500:
            self.right(7)
        if key[pygame.K_RIGHT] == 1 and ninja.rect.y <= 500:
            self.left(7)

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bomb_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH+random.randint(100,200)
        self.rect.y = land_pos[len(land_pos)-1]-200
    def right(self,sp):
        self.rect.x += sp
    def left(self,sp):
        self.rect.x -= sp
    def touch_n(self):
        self.rect.x = WIDTH+random.randint(100,200)
        self.rect.y = land_pos[len(land_pos)-1]-200
    def update(self):
        global jump
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == 1 and ninja.rect.y <= 500:
            self.right(7)
        if key[pygame.K_RIGHT] == 1 and ninja.rect.y <= 500:
            self.left(7)
        if self.rect.x <= -60:
            self.rect.x = WIDTH+random.randint(100,1000)
            self.rect.y = land_pos[len(land_pos)-1]-200

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = rocket_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = -50
    def right(self,sp):
        self.rect.x += sp
    def left(self,sp):
        self.rect.x -= sp
    def update(self):
        global draw
        if draw != 100:
            self.rect.x = WIDTH
            draw = random.randint(1,2000)
        if draw == 100 and not self.rect.x <= -600:
            if self.rect.x <= -600:
                draw = 1
                self.rect.x = WIDTH
            else:
                self.rect.x -= 10
                draw_text(screen,"score: "+str(score),30,WIDTH/2,0,"black")
                all_sprites.draw(screen)
        else:
            draw = 1
            self.rect.x = WIDTH
            
class Missle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = missle_img
        self.rect = self.image.get_rect()
        self.rect.x = ninja.rect.x+random.randint(0,300)
        self.rect.y = -110
    def right(self,sp):
        self.rect.x += sp
    def left(self,sp):
        self.rect.x -= sp
    def update(self):
        global out
        key = pygame.key.get_pressed()
        if out != 100:
            out = random.randint(1,2000)
        if out == 100:
            if key[pygame.K_LEFT] == 1 and ninja.rect.y <= 500:
                self.right(1)
            if key[pygame.K_RIGHT] == 1 and ninja.rect.y <= 500:
                self.left(5)
            ninja.update()
            if self.rect.y >= 610 or self.rect.x >= 1000 or self.rect.x <= -100:
                out = 1
                self.rect.x = ninja.rect.x+random.randint(0,300)
                self.rect.y = -110
            else:
                self.rect.y += 2
                draw_text(screen,"score: "+str(score),30,WIDTH/2,0,"black")
                all_sprites.draw(screen)
        else:
            out = 1
            self.rect.x = ninja.rect.x+random.randint(0,300)
            self.rect.y = -110
            
all_sprites = pygame.sprite.Group()
landgp = pygame.sprite.Group()
coingp = pygame.sprite.Group()
bombgp = pygame.sprite.Group()
rocketgp = pygame.sprite.Group()
misslegp = pygame.sprite.Group()
pygame.mixer.music.play(-1)
draw_init()
for i in range(1000):
    if i == 0:
        f = 1
    land_locate.append(land_locate[len(land_locate)-1]+250)
    land = Land(land_locate[i])
    landgp.add(land)
    all_sprites.add(land)
    f = 0
ninja = Ninja()
coin = Coin()
bomb = Bomb()
rocket = Rocket()
missle = Missle()
all_sprites.add(ninja)
coingp.add(coin)
bombgp.add(bomb)
rocketgp.add(rocket)
misslegp.add(missle)
all_sprites.add(rocket)
all_sprites.add(missle)
all_sprites.add(ninja)

running = True
while running:
    clock.tick(60)
    for i in pygame.sprite.spritecollide(ninja, landgp, False, pygame.sprite.collide_rect):
        ninja.tl = 1
        ninja.touch_land()
    for i in pygame.sprite.spritecollide(ninja, coingp, False, pygame.sprite.collide_rect):
        ninja.touch_coin()
        coin.touch_n()
    for i in pygame.sprite.spritecollide(ninja, bombgp, False, pygame.sprite.collide_rect):
        ninja.touch_bomb()
        bomb.touch_n()
    for i in pygame.sprite.spritecollide(ninja, rocketgp, False, pygame.sprite.collide_rect):
        key = pygame.key.get_pressed()
        jump = key[pygame.K_SPACE] == 1 or key[pygame.K_UP] == 1
        if jump:
            boom_sd.play()
            lose()
    for i in pygame.sprite.spritecollide(ninja, misslegp, False, pygame.sprite.collide_rect):
        boom_sd.play()
        lose()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fill()
    all_sprites.update()
    coingp.update()
    bombgp.update()
    rocketgp.update()
    misslegp.update()
    all_sprites.draw(screen)
    coingp.draw(screen)
    bombgp.draw(screen)
    ninja.tl = 0
    draw_text(screen,"score: "+str(score),30,WIDTH/2,0,"black")
    pygame.display.flip()
    if score >= 20:
        time.sleep(1)
        win()

pygame.quit()