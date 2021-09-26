# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile


class FileMover:

    def __init__(self, import_folder, out_folder):
        self.import_folder = import_folder
        self.out_folder = out_folder

    def unzip(self):
        zfile = zipfile.ZipFile(self.import_folder, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)


    def get_files(self):

        for dirpath, dirnames, filenames in os.walk(self.import_folder):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                create_year = file_time[0]
                create_month = file_time[1] if len(str(file_time[1])) == 2 else '0' + str(file_time[1])  # двузначный формат
                output_path = os.path.join(self.out_folder, str(create_year), str(create_month))

                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                shutil.copy2(full_file_path, output_path)


import_folder = 'icons'
out_folder = 'icons_by_year'
file_mover = FileMover(import_folder=import_folder, out_folder=out_folder)
# file_mover.unzip()
file_mover.get_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
