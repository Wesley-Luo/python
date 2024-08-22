import pygame
import random
import os
pygame.init()
screen = pygame.display.set_mode((1000,600))


# x = 10
# y = 10

# for i in range(8):
#     for i in range(10):
#         x = x + 100
#         screen.blit(ball_img,(x,y))
#     x = 10
#     y = y + 100

running = True
while running :
    pygame.draw.line(screen,"white", (100,100), (500,500),20)
    pygame.display.flip()
    # screen.blit(ball_img,(random.randint(0,1000),random.randint(0,600)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill("dark green")
    pygame.display.flip()
pygame.quit()