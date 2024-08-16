import pygame
import random
import time
import os
pygame.init()
pygame.display.init()

FPS = 60
SCRN_W = 1000
SCRN_H = 600
PINK = (255,210,230)
block_x = [330, 480, 630, 330, 480, 630, 330, 480, 630]
block_y = [-20, -20, -20, 130, 130, 130, 280, 280, 280]
screen = pygame.display.set_mode((SCRN_W, SCRN_H))
pygame.display.set_caption("圈圈叉叉")
blank_img = pygame.transform.scale((pygame.image.load(os.path.join("tic tac toe","blank.png"))),(150,150))
start_img = pygame.transform.scale((pygame.image.load(os.path.join("tic tac toe","ooxx_start.png"))),(850,600))
win_sound = pygame.mixer.Sound(os.path.join("tic tac toe","Triumph.wav"))
ds = pygame.mixer.Sound(os.path.join("tic tac toe","Clang.wav"))
pygame.mixer.music.load(os.path.join("tic tac toe","Chill.wav"))
screen.fill(PINK)
b_x = 250
b_y = -80
turn_01 = 0
fill = 0
x = 0
y = 0
c = [[0,0,0],
     [0,0,0],
     [0,0,0]]
bl = ["00","01","02","10","11","12","20","21","22"]
win = ""
pygame.display.set_icon(blank_img)

pygame.mixer.music.play(-1)
def draw_init():
    global turn_01,running,start_img,b_x,b_y,block_x,block_y,screen,locate
    locate = (320,430,150,145)
    a =  random.choice(["o","x"])
    if a == "o":
        b = "green"
        turn_01 = 0
    if a == "x":
        b = "red"
        turn_01 = 1
    screen.blit(start_img, (80,0))
    draw_text(screen,a, 250, 390, 300,b)
    pygame.display.update()
    waiting = True
    while waiting:
        running = False
        key = pygame.key.get_pressed()
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if a == "x":
                    pygame.draw.rect(screen,"white",locate)
                    draw_text(screen,"o", 250, 390, 300,"green")
                    turn_01 += 1
                    pygame.display.flip()
                    a = "o"
                else:
                    pygame.draw.rect(screen,"white",locate)
                    draw_text(screen,"x", 250, 390, 300,"red")
                    turn_01 += 1
                    pygame.display.flip()
                    a = "x"
            if ev.type == pygame.QUIT:
                    pygame.quit()    
        if key[pygame.K_SPACE]==1:
            waiting = False
            running = True
            screen.fill("light blue")
            for i in range(3):
                b_y += 150
                screen.blit(blank_img,(b_x,b_y))
                for i in range(3):
                    screen.blit(blank_img,(b_x,b_y))
                    b_x += 150
                b_x = 250
                    
font_name = os.path.join("tic tac toe","font.ttf")
def draw_text(surf, text, size, x, y,color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

draw_init() 
while running:

    mouse_pos = pygame.mouse.get_pos()
    mx = mouse_pos[0]-75
    my = mouse_pos[1]-110

    for y in range(3):
        if c[0][y] == c[1][y] and c[1][y] == c[2][y] and c[1][y] != 0:
            if c[1][y] == "o" or c[1][y] == "x":
                win = c[1][y]
                pygame.draw.line(screen,"black",(block_x[0],block_y[(y)]),(block_x[2],block_y[(y)]),20)
    for x in range(3):
        if c[x][0] == c[x][1] and c[x][1] == c[x][2] and c[x][1] != 0:
            if c[x][1] == "o" or c[x][1] == "x":
                win = c[x][1]
                pygame.draw.line(screen,"black",(block_x[0],block_y[(y)]),(block_x[2],block_y[(y)]),20)
    if c[0][0] == c[1][1] and c[1][1] == c[2][2]:
        if c[1][1] == "o" or c[1][1] == "x":
            win = c[1][1]
    if (c[2][0] == c[1][1] and c[1][1] == c[0][2]):
        if c[1][1] == "o" or c[1][1] == "x":
            win = c[1][1]
            pygame.draw.line(screen,"black",(block_x[0],block_y[(y)]),(block_x[2],block_y[(y)]),20)
    pygame.display.flip()

    if win == "o":
            time.sleep(1)
            screen.fill("light yellow")
            draw_text(screen,"O wins!",250,SCRN_W/2,SCRN_H/2-200,"dark green")
            pygame.display.flip() 
            win_sound.play()
            time.sleep(5)       
            pygame.quit()
    if win == "x":
            time.sleep(1)
            screen.fill("light yellow")
            draw_text(screen,"X wins!",250,SCRN_W/2,SCRN_H/2-200,"red")
            pygame.display.flip()
            win_sound.play()
            time.sleep(5)
            pygame.quit()
            exit()
    if fill == 9 and win == "":
        time.sleep(1)
        screen.fill("orange")
        draw_text(screen,"Draw!",250,SCRN_W/2,SCRN_H/2-200,"black")
        pygame.display.flip()
        ds.play()
        time.sleep(3)
        pygame.quit()
        exit()

    if turn_01 % 2 == 0:     
        turn = "o"
        turn_col = "green"
        draw_text(screen,"o",400,120,-20,"green")
        draw_text(screen,"x",400,SCRN_W-150,-20,"light grey")
    if not turn_01 % 2 == 0:
        turn = "x"
        turn_col = "red"
        draw_text(screen,"x",400,SCRN_W-150,-20,"red")
        draw_text(screen,"o",400,120,-20,"light grey")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0]-(SCRN_W/2)<= 450 and mouse_pos[1]-(SCRN_H/2)<= 450:
            for i in range(9):
                if c[int(bl[i][0])][int(bl[i][1])] == 0:
                    if abs(mx-block_x[i]) <= 70 and abs(my-block_y[i])<= 70:
                        fill = fill+1
                        draw_text(screen, turn,200,block_x[i], block_y[i] ,turn_col)
                        c[int(bl[i][0])][int(bl[i][1])] = turn
                        turn_01 += 1

    pygame.display.update()        
pygame.quit()
print(block_x)
print(block_y)