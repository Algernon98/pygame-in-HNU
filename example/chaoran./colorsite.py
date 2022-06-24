from tkinter import *
from time import sleep
from random import *
from tkinter import messagebox

class Tetris:
    def __init__(self):
        self.color=['red','yellow','orange','purple','pink','green','blue']#设置方块颜色
        # 字典 存储形状对应7种形状 元组存储坐标
        self.shapeDict = {1: [(0, 0), (0, -1), (0, -2), (0, 1)],  # shape I
                          2: [(0, 0), (0, -1), (1, -1), (1, 0)],  # shape ■ 田字格形
                          3: [(0, 0), (-1, 0), (0, -1), (1, 0)],  # shape T T型
                          4: [(0, 0), (0, -1), (1, 0), (2, 0)],  # shape J 右长倒L盖子
                          5: [(0, 0), (0, -1), (-1, 0), (-2, 0)],  # shape L
                          6: [(0, 0), (0, -1), (-1, -1), (1, 0)],  # shape Z
                          7: [(0, 0), (-1, 0), (0, -1), (1, -1)]}  # shape S
