# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (1200, 600)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# x1, y1 = 50, 50
# x2, y2 = 350, 450
#
# for color in rainbow_colors:
#     point1 = sd.get_point(x1, y1)
#     point2 = sd.get_point(x2, y2)
#     sd.line(point1, point2, color=color, width=4)
#     x1 += 5
#     x2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(800, -400)
radius = 800

for color in rainbow_colors:
    sd.circle(point, radius, color, width=15)
    radius += 15

sd.pause()
