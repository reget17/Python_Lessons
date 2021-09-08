# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def geometry_writer(point, lines, key_angle, color, angle=0, length=100):
    if lines == 1:
        pass
        # Придумать как нарисовать финальную линию
        # sd.line(start_point=point, end_point=point, width=1)
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v.draw(color=color)
    angle += key_angle
    lines -= 1
    if lines == 0:
        return
    geometry_writer(point=v.end_point, lines=lines, key_angle=key_angle, angle=angle, length=length, color=color)


color_list = {
    '0': sd.COLOR_RED,
    '1': sd.COLOR_ORANGE,
    '2': sd.COLOR_YELLOW,
    '3': sd.COLOR_GREEN,
    '4': sd.COLOR_CYAN,
    '5': sd.COLOR_BLUE,
    '6': sd.COLOR_PURPLE
}
print('Возможные цвета:')
print('    0: red')
print('    1: orange')
print('    2: yellow')
print('    3: green')
print('    4: cyan')
print('    5: blue')
print('    6: purple')


while True:
    user_input = input('Введите номер желаемого цвета:')
    if user_input in color_list:
        break
    else:
        print('Вы ввели неверный номер')
        continue

user_color = color_list[user_input]
point_0 = sd.get_point(100, 100)
geometry_writer(point_0, key_angle=120, lines=3, length=100, angle=0, color=user_color)



sd.pause()
