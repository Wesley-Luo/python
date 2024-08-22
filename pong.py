import pgzrun
WIDTH = 800                                 # 屏幕宽度
HEIGHT = 600                                # 屏幕高度
PAD_SPEED = 1000 
pad = Rect((20, 20), (10, 100))
def draw():                                 # 游戏绘制函数
    screen.clear()
    screen.draw.filled_rect(pad, 'white')

def update(dt):                             # 游戏更新函数
    listen_key(dt)

def listen_key(dt):                         # 键盘响应
    # if keyboard.w:
    #     pad_1.y -= PAD_SPEED * dt
    #     if pad_1.top < 0:
    #         pad_1.top = 0
    # elif keyboard.s:
    #     pad_1.y += PAD_SPEED * dt
    #     if pad_1.bottom > HEIGHT:
    #         pad_1.bottom = HEIGHT

    if keyboard.up:
        pad.y -= PAD_SPEED * dt
        if pad.top < 0:
            pad.top = 0
    elif keyboard.down:
        pad.y += PAD_SPEED * dt
        if pad.bottom > HEIGHT:
            pad.bottom = HEIGHT
pgzrun.go()
