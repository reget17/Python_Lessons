# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
from pprint import pprint


class BookStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.char_count = 0
        self.sorted_char = []

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_line(line=line[:-1])

    def collect_line(self, line):
        for char in line[:-1]:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1
                self.char_count += 1

    def prepare(self):
        for char, total in self.stat.items():
            self.sorted_char.append([total, char])
        self.sorted_char.sort(reverse=True)

    def print_asc_order(self):
        self.print(sorted_item=self.sorted_char)

    def print_alpha_asc_order(self):
        temp_sorted_char = self.sorted_char
        temp_sorted_char = sorted(temp_sorted_char, key=lambda char: char[1])
        self.print(temp_sorted_char)

    def print_alpha_desc_order(self):
        temp_sorted_char = self.sorted_char
        temp_sorted_char = sorted(temp_sorted_char, key=lambda char: char[1], reverse=True)
        self.print(temp_sorted_char)

    def print(self, sorted_item):
        print(f"+{'+':-^30}+")
        print(f"|{'Буква':^14}|{'Частота':^15}|")
        print(f"+{'+':-^30}+")
        for summ, char in sorted_item:
            print(f'|{char:^14}|{summ:^15}|')
        print(f"+{'+':-^30}+")
        print(f"|{'Итого':^14}|{self.char_count:^15}|")
        print(f"+{'+':-^30}+")


book_stat = BookStat(file_name='voyna-i-mir.txt.zip')
# book_stat = BookStat(file_name='1.txt')
book_stat.collect()
book_stat.prepare()
book_stat.print_asc_order()
book_stat.print_alpha_asc_order()
book_stat.print_alpha_desc_order()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
