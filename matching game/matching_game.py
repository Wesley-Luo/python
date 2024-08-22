import pygame
import random
import time
import os
pygame.init()

WID = 1000
HEI = 600
screen = pygame.display.set_mode((WID, HEI))
pygame.display.set_caption("配對記憶遊戲")
clock = pygame.time.Clock()
cx = 20
cy = 15
flip = 0
card1 = 0
card2 = 0
left = 10
timer = 2460
card1pos = []
card2pos = []
shape_imgs = [pygame.image.load(os.path.join("matching game","costume1.png")),
pygame.image.load(os.path.join("matching game","costume2.png")),
pygame.image.load(os.path.join("matching game","costume3.png")),
pygame.image.load(os.path.join("matching game","costume4.png")),
pygame.image.load(os.path.join("matching game","costume5.png")),
pygame.image.load(os.path.join("matching game","costume6.png")),
pygame.image.load(os.path.join("matching game","costume7.png")),
pygame.image.load(os.path.join("matching game","costume8.png")),
pygame.image.load(os.path.join("matching game","costume9.png")),
pygame.image.load(os.path.join("matching game","costume10.png"))]
none_img = pygame.image.load(os.path.join("matching game","none.png"))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("matching game","match_game_back.png")),(1000,700))
pygame.display.set_icon(none_img)

for i in range(len(shape_imgs)):
    shape_imgs[i] = pygame.transform.scale(shape_imgs[i],(90,130))
none_img = pygame.transform.scale(none_img,(90,130))
n_touch_img = pygame.transform.rotate(none_img,5)

match_sd = pygame.mixer.Sound(os.path.join("matching game","correct_choose.wav"))
boing_sd = pygame.mixer.Sound(os.path.join("matching game","boing.wav"))
wl_sd = [pygame.mixer.Sound(os.path.join("matching game","Triumph.wav")),pygame.mixer.Sound(os.path.join("matching game","Big_Boing.wav"))]

pygame.mixer.music.load(os.path.join("matching game","Drum_Set.wav"))
randoms = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
matchs = []
for i in range(len(randoms)):
    a = random.randint(0,len(randoms)-1)
    matchs.append(randoms[a])
    randoms.pop(a)

def fill():
    screen.blit(back_img,(0,-80))

def win():
    screen.fill("green")
    draw_text(screen,"You win!",200,WID/2,150)
    pygame.display.flip()
    wl_sd[0].play()
    time.sleep(3)
    pygame.quit()
    exit() 

def lose():
    screen.fill("red")
    draw_text(screen,"You lose!",200,WID/2,150)
    draw_text(screen,"("+str(left*2)+" cards left"+")",50,WID/2,400)
    pygame.display.flip()
    wl_sd[1].play()
    time.sleep(3)
    pygame.quit()
    exit()

def refresh():
    global card1,card2,card1pos,card2pos
    card1 = 0
    card2 = 0
    card1pos = []
    card2pos = []

font_name = os.path.join("matching game","font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, "black")
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

class Shape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.flip = 0
        self.pic = shape_imgs[matchs[0]]
        self.num = matchs[0]+1
        self.image = none_img
        self.rect = self.image.get_rect()
        self.rect.x = cx
        self.rect.y = cy
    def update(self):
        global card1,card2,card1pos,card2pos
        if self.rect.collidepoint(pygame.mouse.get_pos()) or self.flip == 1:
            fill()
            self.image = n_touch_img
            if pygame.mouse.get_pressed() == (True,False,False) or self.flip == 1 and (card1 == 0 or card2 == 0):
                self.flip = 1
                self.image = self.pic
                if card1 == 0 and card2pos != [self.rect.x,self.rect.y]:
                    card1 = self.num
                    card1pos = [self.rect.x,self.rect.y]
                elif card2 == 0 and card1pos != [self.rect.x,self.rect.y]:
                    card2 = self.num
                    card2pos = [self.rect.x,self.rect.y]
        else:
            self.image = none_img

allgp = pygame.sprite.Group()
shape = Shape()

for a in range(4):
    shape = Shape()
    allgp.add(shape)
    for i in range(5):
        shape = Shape()
        allgp.add(shape)
        matchs.pop(0)
        cx += 120
    cx = 20
    cy += 145

pygame.mixer.music.play(-1)
run = True
while run:

    if card1 != 0 and card2 != 0:
        if card1 == card2:
            match_sd.play()
            time.sleep(0.5)
            for i in allgp:
                i.flip = 0
                if i.num == card1 or i.num == card2:
                    allgp.remove(i)
            refresh()
            left -= 1
        elif card1 != card2:
            refresh()
            boing_sd.play()
            time.sleep(0.3)
            for i in allgp:
                i.flip = 0
                for i in allgp:
                    i.flip = 0
                    i.image = none_img
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    fill()
    allgp.update()
    allgp.draw(screen)
    timer -= 1
    draw_text(screen, "time: "+ str(int(timer/60)), 35, WID/2+350, 0)
    pygame.display.flip()
    clock.tick(60)

    if left < 1:
        time.sleep(0.5)
        win()
    elif int(timer/60) <= 0:
        time.sleep(0.5)
        lose()

pygame.quit()
exit()