# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __add__(self, other):
        if type(other) == Air:
            return Storm()
        elif type(other) == Fire:
            return Vapor()
        elif type(other) == Earth:
            return Dirt()

    def __str__(self):
        return 'Вода'


class Air:

    def __add__(self, other):
        if type(other) == Fire:
            return Lightning()
        elif type(other) == Earth:
            return Lava()

    def __str__(self):
        return 'Воздух'

class Fire:
    def __str__(self):
        return 'Огонь'

class Earth:
    def __str__(self):
        return 'Земля'

class Storm:

    def __str__(self):
        return 'Шторм'

class Vapor:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'

class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'

class Lava:
    def __str__(self):
        return 'Лава'


print(Air(), '+', Earth(), '=', Air() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
