# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 0
        self.food = 0
        self.cat_food = 30
        self.dirt = 0
        self.coat_count = 0
        self.money_count = 0
        self.food_count = 0
        self.animals = []

    def __str__(self):
        return 'В доме денег - {}, еды - {}, грязи - {}, кошачьей еды - {}'.format(self.money, self.food, self.dirt, self.cat_food)

    def act(self):
        self.dirt += 5

    def get_animal(self, animal):
        self.animals.append(animal)


class Man:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 30
        self.happiness = 100
        self.max_food_per_each = 30

    def __str__(self):
        return '{} здоровье - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food > 0:
            if self.house.food >= self.max_food_per_each:
                self.house.food -= self.max_food_per_each
                self.fullness += self.max_food_per_each
                self.house.food_count += self.max_food_per_each
                cprint('{} поел на {}'.format(self.name, self.max_food_per_each), color='yellow')
            else:
                self.fullness += self.house.food
                self.house.food_count += self.house.food
                cprint('{} поел на {}'.format(self.name, self.house.food), color='yellow')
                self.house.food = 0
        else:
            self.fullness -= 10
            cprint('{} еды нет'.format(self.name), color='red')

    def go_to_house(self, house):
        self.house = house
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} - вы умерли!!!'.format(self.name), color='red')
            return
        if self.happiness < 10:
            cprint('{} - вы умерли от депрессии!!!'.format(self.name), color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10

    def pet_animal(self):
        self.happiness += 5
        self.fullness -= 10
        cprint('{} погладил(а) кота'.format(self.name), color='green')


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 5)

        if self.fullness <= 30 and self.house.food > 0:
            self.eat()
        elif self.house.money <= 100:
            self.work()
        elif self.happiness <= 30:
            self.gaming()
        elif 1 <= dice <= 2:
            self.work()
        elif 3 <= dice <= 4:
            self.gaming()
        elif dice == 5:
            self.pet_animal()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        self.house.money_count += 150
        cprint('{} сходил на работу'.format(self.name), color='blue')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        if self.happiness >= 200:
            self.happiness = 200
        cprint('{} весь день играл в танки'.format(self.name), color='green')


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 4)

        if self.fullness <= 30 and self.house.food > 0:
            self.eat()
        elif self.happiness <= 30 and self.house.money >= 350:
            self.buy_fur_coat()
        elif self.house.cat_food <= 20:
            self.buy_cat_food()
        elif self.house.food <= 30:
            self.buy_food()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif 1 <= dice <= 2:
            self.pet_animal()
        else:
            cprint('{} ничего не делала в этот день'.format(self.name), color='magenta')

    def buy_food(self):
        self.fullness -= 10
        if self.house.money >= 100 - self.house.food:
            self.house.money -= 100 - self.house.food
            self.house.food = 100
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
        else:
            cprint('{} нет денег на еду!'.format(self.name), color='red')

    def buy_cat_food(self):
        self.fullness -= 10
        if self.house.money >= 100 - self.house.cat_food:
            self.house.money -= 100 - self.house.cat_food
            self.house.cat_food = 100
            cprint('{} сходила в магазин за едой для кота'.format(self.name), color='magenta')
        else:
            cprint('{} нет денег на еду!'.format(self.name), color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            self.happiness += 60
            self.house.money -= 350
            self.house.coat_count += 1
            cprint('{} купила шубу'.format(self.name), color='green')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100 if self.house.dirt >= 100 else 0
        cprint('{} убралась в доме'.format(self.name), color='magenta')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return '{} здоровье - {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif 1 <= dice <= 2:
            self.sleep()
        elif 3 <= dice <= 5:
            self.soil()
        elif dice == 6:
            self.eat()

    def eat(self):
        if self.house.cat_food >= 10:
            if 100 - self.fullness < 10:
                self.house.cat_food -= (100 - self.fullness)//2
                self.fullness = 100
            else:
                self.house.cat_food -= 10
                self.fullness += 20
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} еды нет'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('{} проспал весь день'.format(self.name), color='green')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} драл обои весь день'.format(self.name), color='blue')

    def go_to_the_house(self, house):
        self.house = house
        house.get_animal(self)


class Child (Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.happiness = 100
        self.max_food_per_each = 10

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} - вы умерли!!!'.format(self.name), color='red')
            return
        if self.fullness <= 20:
            self.eat()
        else:
            self.sleep()

    def sleep(self):
        self.fullness -= 10
        cprint('{} проспал весь день'.format(self.name), color='green')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
son = Child(name='Пиздюк')
masha.go_to_house(home)
serge.go_to_house(home)
son.go_to_house(home)
my_cat = Cat('кот Василий')
my_cat.go_to_the_house(home)
my_cat1 = Cat('кот Семён')
my_cat1.go_to_the_house(home)
my_cat2 = Cat('кот Мурзик')
my_cat2.go_to_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    son.act()
    home.act()
    my_cat.act()
    my_cat1.act()
    my_cat2.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(son, color='cyan')
    cprint(home, color='cyan')
    cprint(my_cat, color='cyan')
    cprint(my_cat1, color='cyan')
    cprint(my_cat2, color='cyan')

cprint('Всего съедено еды - {}, заработано денег - {}, куплено шуб - {}'.
       format(home.food_count, home.money_count, home.coat_count))


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов





######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

