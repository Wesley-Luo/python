import pygame
import random
import time
import os

pygame.init()
pygame.display.set_caption("打磚塊")

brick_x = 10
brick_y = 10
ball_pos_x = 0
ball_pos_y = 0
player_x = 0
left = 66

SCRN_W = 1000
SCRN_H = 600
FPS = 60
WHITE = ((255,255,255))

font_name = os.path.join("break out","font.ttf")
start_img = pygame.image.load(os.path.join("break out","start.png"))
ball_img = pygame.transform.scale(pygame.image.load(os.path.join("break out","ball.gif")),(50,50))
win_sound = pygame.mixer.Sound(os.path.join("break out","win.wav"))
lose_sound = pygame.mixer.Sound(os.path.join("break out","lose.wav"))
pop_sound = pygame.mixer.Sound(os.path.join("break out","Pop.wav"))
pygame.mixer.music.load(os.path.join("break out","Dance Funky.wav"))
pygame.mixer.music.set_volume(0.5)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCRN_W,SCRN_H))
speed = [5, 5]
pygame.display.set_icon(ball_img)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = 10
        self.width = 150
        self.speedx = 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width()-self.width)/2
        self.rect.y = screen.get_height()-self.height-15

    def update(self):
        global player_x
        key_pressed = pygame.key.get_pressed()
        if self.rect.centerx >= SCRN_W-self.width/2:
            self.rect.centerx = SCRN_W-self.width/2
        if self.rect.x <= 0:
            self.rect.x = 0
        if key_pressed[pygame.K_RIGHT]:
            self.rect.centerx += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.centerx -= self.speedx
        player_x = self.rect.centerx 
    
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = 40
        self.width = 150
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width()-self.width)/2+50
        self.rect.y = screen.get_height()-self.height-50

    def update(self):
        global ball_pos_x , ball_pos_y
        self.rect = self.rect.move(speed)
        if self.rect.left < 0 or self.rect.right > SCRN_W:
            speed[0] = - speed[0]
        if  (self.rect.bottom-self.height)< 0:
            speed[1] = - speed[1]
        if self.rect.bottom > (SCRN_H-40) and (abs(self.rect.centerx - player_x) < 150) and not self.rect.bottom > (SCRN_H-15):
            speed[1] = - speed[1]
        if self.rect.bottom > (SCRN_H-40) and (abs(self.rect.bottomleft[0]-player_x)<= 5 or abs(self.rect.bottomright[0]-player_x)<= 5) and abs(self.rect.centerx-player_x)>= 75:
            speed[0] = - speed[0]
        ball_pos_x = self.rect.centerx
        ball_pos_y = self.rect.centery

    def hit(self):
        global speed
        self.rect = self.rect.move(speed)
        speed[1] = - speed[1]
        if self.rect.left < 0 or self.rect.right > SCRN_W:
            speed[0] = - speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCRN_H :
            speed[1] = - speed[1]
        if self.rect.bottom > (SCRN_H-40) and (abs(self.rect.centerx - player_x) < 75) and not self.rect.bottom > (SCRN_H-15):
            speed[1] = - speed[1]

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = 40
        self.width = 80
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((random.randint(50,255),random.randint(40,255),random.randint(50,255)))
        self.rect = self.image.get_rect()
    def pos(self,brick_x,brick_y):
        self.rect.x = brick_x
        self.rect.y = brick_y

def draw_text(surf,text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

pygame.mixer.music.play(-1)
def draw_init():
    star_img = pygame.transform.scale(start_img, (1600,1200))
    screen.blit(star_img, (-300,-310))
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:
                waiting = False
                return False
            
draw_init()        
show_init = True        
all_sprites_list = pygame.sprite.Group()
brick_group = pygame.sprite.Group()
player = Player()
ball = Ball()
all_sprites_list.add(player)
all_sprites_list.add(ball)

for i in range(6):
    for i in range(11):
        brick = Brick()
        brick.pos(brick_x ,brick_y)
        all_sprites_list.add(brick)
        brick_group.add(brick)
        brick_x = brick_x + 90
    brick_x = 10
    brick_y = brick_y + 50

running = True
while running:

    clock.tick(FPS)
    rock_hit = pygame.sprite.spritecollide(ball, brick_group, True, pygame.sprite.collide_circle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break

    for _ in rock_hit:
        left -= 1
        ball.hit()
        pop_sound.play()

    if ball_pos_y >= SCRN_H or left == 0:
        running = False    
        break

    all_sprites_list.update()
    screen.fill("black")
    all_sprites_list.draw(screen)
    pygame.display.flip()

    if show_init:
        time.sleep(1)
        show_init = False

if ball_pos_y >= SCRN_H:
    screen.fill("red")
    draw_text(screen, "You lose!", 200, 500, 150)
    lose_sound.play()    
elif SCRN_H or left == 0:
    screen.fill("dark green")
    draw_text(screen, "You win!", 200, 500, 150)
    win_sound.play()

pygame.display.flip()
time.sleep(3)
pygame.quit()
exit()