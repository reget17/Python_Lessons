# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class RegProtocol:

    def __init__(self, input_file):
        self.input_file = input_file
        self.registrations_good = 'registrations_good.log'
        self.registrations_bad = 'registrations_bad.log'

    def start(self):
        with open(self.input_file, 'r', encoding='UTF8') as file:
            for line in file:
                line = line[:-1]
                try:
                    self.validate(line=line)
                    self.write_good(line)
                except ValueError as exc:
                    self.write_bad(line, mistake='ValueError', arg=exc)
                except NotNameError as exc:
                    self.write_bad(line, mistake='NotNameError', arg=exc)
                except NotEmailError as exc:
                    self.write_bad(line, mistake='NotEmailError', arg=exc)

    def validate(self, line):
        line_list = line.split(sep=' ')

        if len(line_list) != 3:
            raise ValueError('Введены не все 3 поля')
        elif not line_list[0].isalpha():
            raise NotNameError('В имени не только буквы')
        elif not ('@' in line_list[1] and '.' in line_list[1]):
            raise NotEmailError('Ошибка в email')
        elif not 10 <= int(line_list[2]) <= 99:
            raise ValueError('Некорректный возраст')

    def write_good(self, text):
        with open(self.registrations_good, 'a', encoding='UTF8') as file:
            file.write(text)
            file.write('\n')

    def write_bad(self, text, mistake, arg=None):
        with open(self.registrations_bad, 'a', encoding='UTF8') as file:
            file.write(f'{text} | {mistake} | {arg}')
            file.write('\n')

    def clean_files(self):
        with open(self.registrations_bad, 'w') as file:
            file.write('')
        with open(self.registrations_good, 'w') as file:
            file.write('')


file = 'registrations.txt'
myfile = RegProtocol(file)
myfile.clean_files()
myfile.start()



