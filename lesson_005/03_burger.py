# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger.bread
import my_burger.cutlet
import my_burger.cucumber
import my_burger.tomato
import my_burger.mayo
import my_burger.cheese

my_burger.bread.add_item()
my_burger.cutlet.add_item()
my_burger.cucumber.add_item()
my_burger.tomato.add_item()
my_burger.mayo.add_item()
my_burger.cheese.add_item()
my_burger.bread.add_item()

