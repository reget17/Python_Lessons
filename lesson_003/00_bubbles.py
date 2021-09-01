# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, width=1)


# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    bubble(point, 10)

sd.pause()
