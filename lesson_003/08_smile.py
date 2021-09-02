# -*- coding: utf-8 -*-

# (определение функций)
from random import random

import simple_draw
import random
import math
import numpy as np

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(point_x, point_y, color):
    ellipse_point_left = simple_draw.get_point(point_x - 70, point_y - 50)
    ellipse_point_right = simple_draw.get_point(point_x + 70, point_y + 50)
    simple_draw.ellipse(ellipse_point_left, ellipse_point_right, color, width=1)

    circle_point_left = simple_draw.get_point(point_x - 30, point_y + 10)
    circle_point_right = simple_draw.get_point(point_x + 30, point_y + 10)
    simple_draw.circle(circle_point_left, 5, width=1)
    simple_draw.circle(circle_point_right, 5, width=1)

    # улыбка
    smile_radius = 30
    smile_coordinates = []

    for i in np.arange(3.9, 5.5, 0.1):
        smile_x = round(smile_radius * math.cos(i))
        smile_y = round(smile_radius * math.sin(i))
        smile_coordinates.append(simple_draw.get_point(point_x + smile_x, point_y + smile_y))
    simple_draw.lines(smile_coordinates, color, width=1)


for _ in range(10):
    x = random.randint(50, 550)
    y = random.randint(50, 550)
    smile(x, y, simple_draw.COLOR_YELLOW)


simple_draw.pause()
