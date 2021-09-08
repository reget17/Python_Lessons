# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def lines_writer(point, color, lines, key_angle, angle=0, length=100):
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v.draw(color=color)
    angle += key_angle
    lines -= 1
    if lines == 1:
        return v.end_point
    end_point = lines_writer(point=v.end_point, lines=lines, key_angle=key_angle, angle=angle, length=length, color=color)
    return end_point


def figure_writer (point, figure_id, color, length, angle):
    end_point = None
    if figure_id == '0':
        end_point = lines_writer(point=point, color=color, angle=angle, length=length, lines=3, key_angle=120)
    elif figure_id == '1':
        end_point = lines_writer(point=point, color=color, angle=angle, length=length, lines=4, key_angle=90)
    elif figure_id == '2':
        end_point = lines_writer(point=point, color=color, angle=angle, length=length, lines=5, key_angle=72)
    elif figure_id == '3':
        end_point = lines_writer(point=point, color=color, angle=angle, length=length, lines=6, key_angle=60)
    sd.line(start_point=end_point, end_point=point, width=1, color=color)


color_list = {
    '0': sd.COLOR_RED,
    '1': sd.COLOR_ORANGE,
    '2': sd.COLOR_YELLOW,
    '3': sd.COLOR_GREEN,
    '4': sd.COLOR_CYAN,
    '5': sd.COLOR_BLUE,
    '6': sd.COLOR_PURPLE
}

figure_list = {
    '0': 'triangle',
    '1': 'square',
    '2': 'pentagon',
    '3': 'hexagon'
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
    user_input_color = input('Введите номер желаемого цвета:')
    if user_input_color in color_list:
        break
    else:
        print('Вы ввели неверный номер')
        continue

print('Возможные фигуры:')
print('    0: triangle')
print('    1: square')
print('    2: pentagon')
print('    3: hexagon')

while True:
    user_input_figure = input('Введите номер желаемой фигуры:')
    if user_input_figure in figure_list:
        break
    else:
        print('Вы ввели неверный номер')
        continue

user_color = color_list[user_input_color]
point_0 = sd.get_point(250, 250)
figure_writer(point_0, user_input_figure, color=user_color, length=100, angle=0)

sd.pause()
