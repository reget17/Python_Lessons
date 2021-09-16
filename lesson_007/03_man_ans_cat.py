# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме осталось {} еды, {} деняк.' \
               'В доме {} кошачьей еды и {} грязи.'.format(self.food, self.money,self.cat_food, self.dirt)


class Man:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.cat = None
        self.fullness = 50

    def __str__(self):
        return 'Я - {}. Сытость - {}'.format(self.name, self.fullness)

    def go_to_house(self, house):
        self.house = house
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 100
        self.fullness -= 10

    def watch_tv(self):
        cprint('{} весь день смотрел TV'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            self.house.food += 50
            self.house.money -= 50
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
        else:
            cprint('{} - деньги кончились!'.format(self.name), color='red')

    def find_cat(self, cat):
        self.cat = cat
        self.cat.owner = self.name
        self.cat.go_to_the_house(self.house)

    def buy_cat_food(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.cat_food += 50
            cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
        else:
            cprint('{} - деньги кончились!'.format(self.name), color='red')

    def clean_the_house(self):
        if self.fullness >= 30:
            self.fullness -= 20
            self.house.dirt -= 100
            cprint('{} убрался в квартире'.format(self.name), color='magenta')
        else:
            cprint('{} - недостаточно энергии'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер.. RIP'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.cat_food < 20:
            self.buy_cat_food()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 10:
            self.work()
        elif self.house.dirt >= 100:
            self.clean_the_house()
        elif dice == 1 or dice == 2:
            self.work()
        else:
            self.watch_tv()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.owner = None

    def __str__(self):
        return 'Я - {}, сытость - {}'.format(self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} нашёл кота'.format(self.owner), color='cyan')
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def eat(self):
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.fullness += 20
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет кошачьей еды'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('{} проспал весь день'.format(self.name), color='green')

    def tear_up_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} драл обои весь день'.format(self.name), color='blue')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif 1 <= dice <= 3:
            self.sleep()
        elif 4 <= dice <= 6:
            self.tear_up_wallpaper()



citizens = [
    Man('Вася'),
]

cats = [
    Cat('кот Мурзик'),
    Cat('кот Семён'),
    Cat('кот Тимофей')

]

my_house = House()

for citizen in citizens:
    citizen.go_to_house(my_house)

for cat in cats:
    citizens[0].find_cat(cat)
    citizens.append(cat)

for day in range(1, 366):
    print('===================== День {} ======================'.format(day))
    for citizen in citizens:
        citizen.act()
        print(citizen)
    print(my_house)



# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
