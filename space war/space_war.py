import pygame
import random
import time
import os
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("太空大戰爭")

FPS = 60
score = 0
life = 5
bg_y = 0
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
start_img = pygame.image.load(os.path.join("space war","Stars.png"))
backdrop_img1 = pygame.image.load(os.path.join("space war", "backdrop1.png"))
backdrop_img2 = pygame.image.load(os.path.join("space war", "backdrop2.png"))
player_img = pygame.image.load(os.path.join("space war", "player.png"))
rock_img = pygame.image.load(os.path.join("space war", "rock.png"))
coin_img = pygame.image.load(os.path.join("space war", "coin.png"))
win_sound = pygame.mixer.Sound(os.path.join("space war","win.wav"))
lose_sound = pygame.mixer.Sound(os.path.join("space war","lose.wav"))
boom_sound = pygame.mixer.Sound(os.path.join("space war","boom.wav"))
coin_sound = pygame.mixer.Sound(os.path.join("space war","Coin.wav"))
pygame.mixer.music.load(os.path.join("space war","Dance Space.wav"))
pygame.mixer.music.set_volume(0.5)
RED = ((255, 0, 0))
YELLOW = ((255,0,255))
BLACK = ((0,0,0))
WHITE = ((255,255,255))
GRAY = ((100,100,100))
BLUE = ((0,255,0))
pygame.display.set_icon(player_img)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 80
        self.height = 80
        self.image = pygame.transform.scale(player_img, (self.width,self.height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.speedx = 7
        self.rect.x = (screen.get_width()-self.width)/2
        self.rect.y = screen.get_height()-self.height-5
    def update(self):
        if running == True :
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if key_pressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if self.rect.x >= screen.get_width()-self.width:
                self.rect.x = screen.get_width()-self.width
            if self.rect.x <= 0:
                self.rect.x = 0

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(rock_img, (self.width,self.height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedy = random.randint(4,10)
        self.rect.x = random.randint(0,screen.get_width()-self.width)
        self.rect.y = 0
    def update(self):
        self.rect.y += self.speedy
        if running == True :
            if self.rect.y >= screen.get_height():
                self.rect.x = random.randint(0,screen.get_width()-self.width)
                self.rect.y = 0

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 60
        self.height = 65
        self.image = pygame.transform.scale(coin_img, (self.width,self.height))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.speedy = random.randint(5,10)
        self.rect.x = random.randint(0,screen.get_width()-self.width)
        self.rect.y = 0
    def update(self):
        global bg_y, screen
        self.rect.y += self.speedy
        if running == True :
            if self.rect.y >= screen.get_height():
                self.rect.x = random.randint(0,screen.get_width()-self.width)
                self.rect.y = 0

all_sprites_list = pygame.sprite.Group()
rock_group = pygame.sprite.Group() 
coin_group = pygame.sprite.Group()
for _ in range(5):
    rock = Rock()
    coin = Coin()
    all_sprites_list.add(rock)
    all_sprites_list.add(coin)
    rock_group.add(rock)
    coin_group.add(coin)
player = Player()
all_sprites_list.add(player)

font_name = os.path.join("space war","font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_init():
    star_img = pygame.transform.scale(start_img, (1350,700))
    screen.blit(star_img, (-185,-30))
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False
            
show_init = True
pygame.mixer.music.play(-1)
running = True
while running:
    clock.tick(FPS)
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
    rock_hit = pygame.sprite.spritecollide(player, rock_group, True, pygame.sprite.collide_circle)
    coin_hit = pygame.sprite.spritecollide(player, coin_group, True, pygame.sprite.collide_circle)
    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break

    all_sprites_list.update()
    bg_y = (bg_y+3)%600
    screen.blit(backdrop_img2,(0,(bg_y-600)))
    screen.blit(backdrop_img1,(0,bg_y))

    for _ in rock_hit:
        rock = Rock()
        all_sprites_list.add(rock)
        rock_group.add(rock)
        life -= 1
        boom_sound.play()

    for _ in coin_hit:
        coin = Coin()
        all_sprites_list.add(coin)
        coin_group.add(coin)
        score += 1
        coin_sound.play()
        
    if score >= 100 or life <= 0 :
        running = False
        break
    
    draw_text(screen, "score: "+(str(score)), 20, 560, 20)
    draw_text(screen, "life: "+(str(life)), 20, 480, 20)
    all_sprites_list.draw(screen)
    pygame.display.flip()

if score >= 100 :
    screen.blit(backdrop_img1,(0,0))
    draw_text(screen, "You win!", 200, 500, 150)
    win_sound.play()
elif life <= 0 :
    screen.blit(backdrop_img2,(0,0))
    draw_text(screen, "You lose!", 200, 500, 150)
    lose_sound.play()
    
draw_text(screen, "score: "+(str(score)), 20, 560, 20)
draw_text(screen, "life: "+(str(life)), 20, 460, 20)
pygame.display.flip()
time.sleep(3)
pygame.quit()
exit()