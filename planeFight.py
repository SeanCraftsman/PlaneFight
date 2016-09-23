# -*- coding: utf8 -*-



SCREEN_SIZE = (380,680)
 

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,20) # 控制窗口打开位置
from ClassOfPlaneFight import *
from init import *


pygame.init() #初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("PlaneFight!")
pygame.mouse.set_visible(False) # 隐藏鼠标指针

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像

clock = pygame.time.Clock()
bullet = []
for i in range(6):
    bullet.append(Bullet())
interval_bullet = 25 #发射子弹的帧数间隔
index_bullet = 0 #初始化子弹坐标
enemy = []
for i in range(10):
    enemy.append(Enemy())
interval_enemy = 100 #敌机出现的间隔
index_enemy = 0 #初始化敌机坐标

while True:
#游戏主循环
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
    time_passed = clock.tick(100)
    time_passed_seconds = time_passed/1000.0
    screen.blit(background, (0,0))
    #将背景图画上去
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    interval_bullet -= 1
    if interval_bullet <= 0:
        interval_bullet = 25
        bullet[index_bullet].restart()#重置子弹
        index_bullet = (index_bullet + 1) % 6 #循环递增
        
    for b in bullet:
        if b.active:
            b.move(time_passed_seconds)#移动子弹
            screen.blit(b.image, (b.x, b.y))#显示子弹

    interval_enemy -= 1
    if interval_enemy <= 0:
        interval_enemy = randint(30,100)
        enemy[index_enemy].restart() #重置飞机
        index_enemy = (index_enemy + 1) % 10 #循环递增
    for e in enemy:
        if e.active:
            e.move(time_passed_seconds) #移动敌机
            screen.blit(e.image, (e.x, e.y)) #显示敌机

    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
 
    pygame.display.update()
    #刷新一下画面