# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
from pprint import pprint


class FileAnalysis:

    def __init__(self, input_file, out_file):
        self.input_file = input_file
        self.output_file = out_file
        self.filtered_text = {}
        self.group_text = {}


    def import_file(self):
        with open(self.input_file, 'r', encoding='cp1251') as file:
            for line in file:
                self.filter_text(line)

    def filter_text(self, line):
        if 'NOK' in line:
            temp_line = line[:17] + ']'
            if temp_line in self.filtered_text:
                self.filtered_text[temp_line] += 1
            else:
                self.filtered_text[temp_line] = 1

    def group(self, mode):
        user_mode = 0
        self.group_text = {}
        if mode == 'hour':
            user_mode = -4
        elif mode == 'month':
            user_mode = -10
        elif mode == 'year':
            user_mode = 5
        else:
            print('Вы ввели некорректный режим для группировки. Введите hour, month или year')
        for date, count in self.filtered_text.items():
            temp_date = date[:user_mode] + ']'
            if temp_date in self.group_text:
                self.group_text[temp_date] += count
            else:
                self.group_text[temp_date] = count


    def writing_file(self):
        with open(self.output_file, 'w', encoding='cp1251') as file:
            content = ''
            for date, count in self.group_text.items():
                content += f'{date} {count}\n'
            file.write(content)
            pprint(content)


input_file = 'events.txt'
output_file = 'out.txt'
file = FileAnalysis(input_file, output_file)
file.import_file()
file.group(mode='hour')
# file.group(mode='month')
# file.group(mode='year')
file.writing_file()



