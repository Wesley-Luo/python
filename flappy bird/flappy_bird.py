import pygame
import random
import time
import os
pygame.init()
pygame.display.set_caption("飛飛鳥")
WIDTH = 1000
HEIGHT = 600
score = 0
rx = -5
font_name = os.path.join("flappy bird","font.ttf")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_img = pygame.transform.scale(pygame.image.load(os.path.join("flappy bird","background.png")),(1020,610))
bird_img = pygame.transform.scale(pygame.image.load(os.path.join("flappy bird","bird.png")),(40,30))
pillar_img = pygame.transform.scale(pygame.image.load(os.path.join("flappy bird","pillar.png")),(50,850))
coin_img = pygame.image.load(os.path.join("flappy bird","bird_coin.png"))
st_img = pygame.image.load(os.path.join("flappy bird","start_background.png"))
s_img = pygame.image.load(os.path.join("flappy bird","sta.png"))
hit_sd = pygame.mixer.Sound(os.path.join("flappy bird","bird_hit.wav"))
coin_sd = pygame.mixer.Sound(os.path.join("flappy bird","collect.wav"))
win_sd = pygame.mixer.Sound(os.path.join("flappy bird","win.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("flappy bird","lose.wav"))
pygame.mixer.music.load(os.path.join("flappy bird","back_music.wav"))
pygame.display.set_icon(bird_img)

class Bird:
    def __init__(self):
        self.x = 40
        self.y = HEIGHT/2-50
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] == 1 and self.y >= -2:
            self.y -= 0.5
        self.y += 0.2
        screen.blit(bird_img,(self.x,self.y))
        if abs((pillar.y+425)-(self.y))>= 40 and abs(self.x-pillar.x)<= 35 or self.y >= HEIGHT-30:
            screen.blit(bird_img,(self.x,self.y))
            hit_sd.play()
            lose()

class Pillar:
    def __init__(self):
        self.x = WIDTH+100
        self.y = random.randint(-250,0)
    def update(self):
        self.x -= 0.5
        if self.x <= -500:
            self.change()
            self.x = WIDTH+100
        screen.blit(pillar_img,(self.x,self.y))
    def change(self):
        self.y = random.randint(-250,0)

class Coin:
    def __init__(self):
        self.x = WIDTH+500
        self.place = 100
        self.y = random.randint(self.place,HEIGHT-self.place)
    def update(self):
        global score
        self.x -= 0.5
        if abs(bird.x-self.x)<= 40 and abs(bird.y*2-self.y*2)<= 40:
            score += 1
            self.change()
            self.x = WIDTH+500
            coin_sd.play()
        elif self.x <= -300:
            self.change()
            self.x = WIDTH+500
        screen.blit(coin_img,(self.x,self.y))
    def change(self):
        self.y = random.randint(self.place,HEIGHT-self.place)

def draw_text(surf,text,size,x,y,col):
    global font_name
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text,True,col)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    screen.blit(text_surface, text_rect)

def win():
    time.sleep(1)
    screen.blit(background_img,(-5,-5))
    draw_text(screen,"You win!",200,WIDTH/2,150,"dark green")
    pygame.display.flip()
    win_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()
def lose():
    time.sleep(1)
    screen.blit(background_img,(-5,-5))
    draw_text(screen,"You lose!",200,WIDTH/2,150,"red")
    pygame.display.flip()
    lose_sd.play()
    time.sleep(3)
    pygame.quit()
    exit()

def draw_init():
    ind = 0
    sta_img = pygame.transform.scale(st_img,(850,600))
    satt_img = pygame.transform.scale(s_img,(1000,600))
    screen.blit(background_img,(-5,-5))
    screen.blit(sta_img, (75,0))
    pygame.display.update()
    waiting = True
    while waiting:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] == 1 and ind == 1:
            waiting = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(satt_img,(0,-5))
                draw_text(screen,"按空白鍵開始遊戲>>>",40,WIDTH/2,350,"black")
                pygame.display.update()
                ind = 1

pygame.mixer.music.play(-1)
draw_init()
screen.blit(background_img,(-5,-5))
pygame.display.flip()
bird = Bird()
pillar = Pillar()
coin = Coin()     
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rx -= 0.3
    rx = rx%1000
    screen.blit(background_img,(rx,-5))
    screen.blit(background_img,(rx-1000,-5))
    bird.update()
    pillar.update()
    coin.update()
    draw_text(screen,"score: "+str(score),30,WIDTH/2,0,"black")
    if score >= 10:
        win()
    pygame.display.flip()
pygame.quit()