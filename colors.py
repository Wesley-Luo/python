fill = ["blue","green","purple","yellow","red","brown","pink"]
i = 0
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((0, 0))
running = True
while running:
    i += 1
    i = i%len(fill)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(1)
    screen.fill(fill[i])
    pygame.display.flip()
pygame.quit()