import pygame
import random
import time
import os

pygame.init()
SIZE = 150
WIDTH = 1000
HEIGHT = 600
FPS = 60
h_img = 0
cr_x = -170
cr_y = -130
pict = 0
touch = 0
score = 0
tmr = 0
timer = 610
press = 0 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("打地鼠")
pygame.mixer.music.load(os.path.join("whack a mole","mole_music.wav"))
wl_sd = [pygame.mixer.Sound(os.path.join("whack a mole","lose.wav")),pygame.mixer.Sound(os.path.join("whack a mole","win.wav"))]
hit_sound = pygame.mixer.Sound(os.path.join("whack a mole","hit.wav"))
st_img = pygame.image.load(os.path.join("whack a mole","start_pic.png"))
b_img = pygame.transform.scale(pygame.image.load(os.path.join("whack a mole","land.png")),(1001,601))
hammer_imgs = [pygame.image.load(os.path.join("whack a mole","hammer1.png")),pygame.image.load(os.path.join("whack a mole","hammer2.png"))]
mole_imgs = [pygame.image.load(os.path.join("whack a mole","mole_in.png")),
             pygame.image.load(os.path.join("whack a mole","mole_out.png")),
            pygame.image.load(os.path.join("whack a mole","mole_hit.png")),]
mole_imgs[0] = pygame.transform.scale(mole_imgs[0],(SIZE,84))
pygame.display.set_icon(hammer_imgs[0])

for i in range(len(mole_imgs)):
    if i != 0:
        mole_imgs[i] = pygame.transform.scale(mole_imgs[i],(SIZE,SIZE))

class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def update(self,himg,mpx,mpy):
        screen.blit(hammer_imgs[himg],(mpx,mpy))

class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = cr_x
        self.y = cr_y
        self.tmr = 0
        self.chtm = 0
        self.fy = self.y+75
        self.pic = 1  
    def update(self):
        global screen,mole_imgs,pict,touch,mpx,mpy,hit_sound,press,score
        up = 100
        if self.pic != 2:
            self.tmr += 1
        if self.tmr >= random.randint(100,500):
            self.pic = random.choice([0,1])
            self.tmr = 0 
        if self.pic == 2:
            self.chtm += 1
            if self.chtm >= 70:
                screen.blit(mole_imgs[0],(self.x,self.y))
                self.pic = 0
                self.chtm = 0
            else:
                self.pic = 2

        pict = self.pic
        if self.pic != 0:
            screen.blit(mole_imgs[self.pic],(self.x,self.y))
        else:
            screen.blit(mole_imgs[0],(self.x,self.fy))
        
        if abs(mpx-75-self.x-75) <= up and abs(mpy-75-self.y-75) <= up and self.pic == 1:
            touch = 1
            if press == 1:
                self.pic = 2
                score += 1
                touch = 0
                press = 0
                hit_sound.play()
        else:
            touch = 0

font_name = os.path.join("whack a mole","font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, "black")
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_init():
    sta_img = pygame.transform.scale(st_img,(1000,750))
    screen.blit(sta_img, (0,-70))
    pygame.display.update()
    waiting = True
    while waiting:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] == 1:
            waiting = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                waiting = False
                pygame.quit()

pygame.mixer.music.play(-1)
draw_init()
screen.blit(b_img,(0,0))
pygame.display.update()
allgp = pygame.sprite.Group()
molegp = pygame.sprite.Group()
hammer = Hammer()
for i in range(3):
    cr_x = -170
    cr_y += 180
    for i in range(5):
        cr_x += 190
        mole = Mole()
        allgp.add(mole)
        molegp.add(mole)
allgp.add(hammer) 

running = True
while running:
    tmr += 1
    m_pos = list(pygame.mouse.get_pos())
    mpx = m_pos[0]
    mpy = m_pos[1]
    m_pos[0] -= 60
    m_pos[1] -= 90

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            press = 1
            h_img = 1
        else:
            press = 0
            h_img = 0

    if pict >= 1 and pict != 2 and press == 1 and touch == 1:
        press = 0
    for i in range(5):
        screen.blit(b_img,(0,0))
        molegp.update()
    hammer.update(h_img,m_pos[0],m_pos[1])

    if score >= 30:
        screen.blit(b_img,(0,0))
        draw_text(screen, "score: 30", 35, WIDTH/2-80, 0)
        time.sleep(1)
        screen.fill("dark green")
        draw_text(screen, "You win!", 200, WIDTH/2,150)
        pygame.display.flip()
        wl_sd[1].play()
        time.sleep(3)
        pygame.quit()
        exit()
    if timer <= 0:
        screen.blit(b_img,(0,0))
        draw_text(screen, "timer: 0", 35, WIDTH/2+80, 0)
        time.sleep(1)
        screen.fill("red")
        draw_text(screen, "Time's up!", 150, WIDTH/2,100)
        draw_text(screen, "You lose!", 150, WIDTH/2,270)
        pygame.display.flip()
        wl_sd[0].play()
        time.sleep(3)
        pygame.quit()
        exit()
    
    draw_text(screen, "score: "+ str(score), 35, WIDTH/2-80, 0)
    draw_text(screen, "timer: "+ str(int(timer/15)), 35, WIDTH/2+80, 0)
    pygame.display.flip()
    clock.tick(FPS)
    timer -= 1

pygame.quit()