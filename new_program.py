import os
import psutil
import sys

print("Это моя первая программа")
print("Привет программист!")

name = input("Введите ваше имя: ")
print(name, ", добро пожаловать!")

inputUser = input("Давайте поработаем? (Y/N)")
if inputUser == 'y':
    while inputUser != 'q':
        print("\nСписок возможностей:")
        print("  [1] - вывести список файлов текущей директории")
        print("  [2] - вывести информацию о системе")
        print("  [3] - показать список запущенных процессов")
        print("  [q] - выход")
        inputUser = input("Выберите возможность: ")
        if inputUser == '1':
            print("Список файлов: ", os.listdir())
        elif inputUser == '2':
            print("Текущая директория: ", os.getcwd())
            print("Операционная система: ", sys.platform)
            print("Кодировка файловой системы: ", sys.getfilesystemencoding())
            print("Пользователь: ", os.getlogin())
            print("Количество процессоров: ", psutil.cpu_count())
        elif inputUser == '3':
            print("Список процессов: ", psutil.pids())
        elif inputUser == 'q':
            print("До новых встреч")
        else:
            print("Неверный ввод")
elif inputUser == 'n' or inputUser == 'q':
    print("До новых встреч")
else:
    print("Неверный ввод")