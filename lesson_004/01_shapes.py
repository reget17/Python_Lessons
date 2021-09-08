# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=1)
#     v2.draw()
#     sd.line(start_point=v2.end_point, end_point=point, width=1)
#
#
# def square(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=1)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=1)
#     v3.draw()
#     sd.line(start_point=v3.end_point, end_point=point, width=1)
#
#
# def pentagon(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=1)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=1)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=1)
#     v4.draw()
#     sd.line(start_point=v4.end_point, end_point=point, width=1)
#
#
# def hexagon(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=1)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=1)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=1)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=1)
#     v5.draw()
#     sd.line(start_point=v5.end_point, end_point=point, width=1)


# def triangle(point, angle=0, length=100):
#     for k in range(0, 241, 120):
#         point = geometry_writer(point, angle+k, length=length)
#
#
# def square(point, angle=0, length=100):
#     for k in range(0, 271, 90):
#         point = geometry_writer(point, angle + k, length=length)
#
#
# def pentagon(point, angle=0, length=100):
#     for k in range(0, 289, 72):
#         point = geometry_writer(point, angle + k, length=length)
#
#
# def hexagon(point, angle=0, length=100):
#     for k in range(0, 301, 60):
#         point = geometry_writer(point, angle + k, length=length)
#
#
# def geometry_writer(point, angle=0, length=100):
#     v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v.draw()
#     return v.end_point


def geometry_writer(point, lines, key_angle, angle=0, length=100):
    if lines == 1:
        pass
        # Придумать как нарисовать финальную линию
        # sd.line(start_point=point, end_point=point, width=1)
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v.draw()
    angle += key_angle
    lines -= 1
    if lines == 0:
        return
    geometry_writer(point=v.end_point, lines=lines, key_angle=key_angle, angle=angle, length=length)


point_0 = sd.get_point(100, 100)
geometry_writer(point_0, key_angle=120, lines=3, length=100, angle=0)

point_1 = sd.get_point(400, 100)
geometry_writer(point_1, key_angle=90, lines=4, length=100, angle=0)

point_2 = sd.get_point(100, 400)
geometry_writer(point_2, key_angle=72, lines=5, length=100, angle=0)

point_3 = sd.get_point(400, 400)
geometry_writer(point_3, key_angle=60, lines=6, length=100, angle=0)

# point_3 = sd.get_point(400, 400)
# hexagon(point_3, length=100, angle=0)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
