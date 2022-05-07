import pygame
import math
import random
import time
import sys
from threading import Thread,Event
import time

from pygame.locals import *
event=Event()
pygame.init()
DISPLAY = pygame.display.set_mode((640, 480))  #初始化游戏界面的大小
pygame.display.set_caption('Ball-Ball')  #给游戏起个标题
FPSLOCK = pygame.time.Clock()   #设置时钟，用来控制游戏进度
BASICFONT = pygame.font.SysFont('arial', 80) #设置字体，第一个参数是字体名称，第二个是字体大小
directions = [1, 2, 3, 4]  #定义方向集合，可以视具体情况增删

# 定义颜色
Black = pygame.Color(0, 0, 0)  #颜色需要自己定义
White = pygame.Color(255, 255, 255)
Red = pygame.Color(255, 0, 0)
Grey = pygame.Color(150, 150, 150)


# 定义玩家控制对象
class Player:
    def __init__(self, x, y, radius):
        self.radius = radius # 半径
        self.x = x # 横坐标
        self.y = y # 纵坐标

    # 画有操控小球
    def drawControlBall(self):
        # for i in control_ball_pos:
        pygame.draw.circle(DISPLAY, White, (control_ball.x, control_ball.y), control_ball.radius) # 操控对象为小球


# 定义无操控小球
class Ball:
    def __init__(self, x, y, radius, direct):
        self.radius = radius
        self.x = x
        self.y = y
        self.direct = direct # 方向（本文只实现了NPC单方向运动的功能）

    def drawUncontrolBall(self):
            pygame.draw.circle(DISPLAY, Red, (self.x, self.y), self.radius)
            if self.direct == 1:
                self.y -= 1
            elif self.direct == 2:
                self.y += 1
            elif self.direct == 3:
                self.x -= 1
            elif self.direct == 4:
                self.x += 1

    def update(self): # 每次被吃掉后需要更新位置


         self.radius = random.randrange(5, 40)
         self.x = random.randrange(self.radius, 640 - self.radius)
         self.y = random.randrange(self.radius, 480 - self.radius)
         self.direct = random.choice(directions)

# 显示分数
def drawScore(score):
    # 设置分数的显示颜色
    score_Surf = BASICFONT.render('%s' % (score), True, Grey)
    # 设置分数的位置
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (320, 0)
    # 绑定以上设置到句柄
    DISPLAY.blit(score_Surf, score_Rect)


# 设置游戏结束
def GameOver():
    # 设置GameOver的显示颜色
    GameOver_Surf = BASICFONT.render('Game Over!', True, Red)
    # 设置GameOver的位置
    GameOver_Rect = GameOver_Surf.get_rect()
    GameOver_Rect.midtop = (320, 240)
    # 绑定以上设置到句柄
    DISPLAY.blit(GameOver_Surf, GameOver_Rect)

    pygame.display.flip()
    # 等待5秒
    time.sleep(5)
    # 退出游戏
    pygame.quit()
    # 退出程序
    sys.exit()


game_flag = True
score = 0
control_ball = Player(200, 100, 20) #初始化玩家
b1 = Ball(100, 100, 10, 2) # 初始化一个NPC
b2 = Ball(300, 200, 20, 3) # 初始化第二个NPC
balls = [b1, b2]
direction = "Right"

while game_flag:
    DISPLAY.fill(Black) # 游戏底色为黑色

    # 绘制出player和npc
    control_ball.drawControlBall()
    b1.drawUncontrolBall()
    b2.drawUncontrolBall()

    drawScore(score)

    # 更新整个待显示的Surface对象到屏幕上
    pygame.display.flip()

    # 控制游戏速度
    FPSLOCK.tick(7)
    for event in pygame.event.get():  # 监听用户的操作
        if event.type == QUIT:

           pygame.quit()
           sys.exit()

    # 判断键盘事件，用 方向键 或 wsad 来表示上下左右
        elif event.type == KEYDOWN:  # KEYDOWM 用于检查用户是否按了键盘
          if event.key == K_UP or event.key == K_w:  # and direction != "DOWN":
            direction = "UP"
          elif event.key == K_DOWN or event.key == K_s:  # and direction != "UP":
            direction = "DOWN"
          elif event.key == K_LEFT or event.key == K_a:  # and direction != "RIGHT":
            direction = "LEFT"
          elif event.key == K_RIGHT or event.key == K_d:  # and direction != "LEFT":
            direction = "RIGHT"

    if direction == "LEFT":
        control_ball.x -= 10
    if direction == "RIGHT":
        control_ball.x += 10
    if direction == "UP":
        control_ball.y -= 10
    if direction == "DOWN":
        control_ball.y += 10

    for ball in balls:
        if (control_ball.x - ball.x) ** 2 + (control_ball.y - ball.y) ** 2 <= (
                ball.radius + control_ball.radius) ** 2: # 俩球相接触，遵循大球吃小球
            if control_ball.radius > ball.radius:
                score = score + 1
                control_ball.radius += 1  # ball.radius
                ball.update()
            elif control_ball.radius <= ball.radius:
               GameOver()

    # 玩家超出游戏界面，则游戏结束
    if control_ball.x < 0 or control_ball.x > 640:
        GameOver()
    if control_ball.y < 0 or control_ball.y > 480:
        GameOver()
