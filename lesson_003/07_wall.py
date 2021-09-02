# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
resolution_height = 600
resolution_width = 600

simple_draw.get_point(resolution_height, 0)
bottom_left_height = resolution_height


for y in range(resolution_height//50):

    if y % 2 == 0:
        top_right_width = -50
    else:
        top_right_width = 0

    bottom_left_height -= 50

    for x in range(resolution_width//100):
        top_right_width += 100
        point_left = simple_draw.Point(top_right_width - 100, bottom_left_height)
        point_right = simple_draw.Point(top_right_width, bottom_left_height + 50)

        simple_draw.rectangle(point_left, point_right, simple_draw.COLOR_BLACK, width=1)




simple_draw.pause()
