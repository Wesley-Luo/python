import pygame
import random
import sys
# 游戏配置
WIDTH = 800
HEIGHT = 600
MOLE_SPEED = 1000  # 地鼠出现或隐藏的速度，单位：毫秒
# 初始化Pygame库
pygame.init()
# 设置游戏窗口
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("打地鼠游戏")
# 地鼠类
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mole1.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(0, height - self.rect.height)
        self.hidden = True
        self.hide_time = 0
    def update(self, delta):
        if self.hidden:
            if pygame.time.get_ticks() - self.hide_time > random.randint(1000, 3000):
                self.hidden = False
                self.rect.x = random.randint(0, width - self.rect.width)
                self.rect.y = random.randint(0, height - self.rect.height)
        else:
            self.hide_time += delta
            if self.hide_time > MOLE_SPEED:
                self.hidden = True
                self.hide_time = 0
# 创建地鼠
mole_group = pygame.sprite.Group()
for _ in range(10):
    mole = Mole()
    mole_group.add(mole)
# 游戏循环
clock = pygame.time.Clock()
running = True
while running:
    delta = clock.tick(60)  # 控制FPS为60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for mole in mole_group:
                if not mole.hidden and mole.rect.collidepoint(event.pos):
                    mole.hidden = True
                    mole.hide_time = 0
    # 更新地鼠状态
    mole_group.update(delta)
    # 渲染绘制
    screen.fill((255, 255, 255))
    for mole in mole_group:
        if not mole.hidden:
            screen.blit(mole.image, mole.rect)
    pygame.display.update()