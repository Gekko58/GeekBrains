import os
import psutil

print("Это моя первая программа")
print("Привет программист!")

name = input("Введите ваше имя: ")
print(name, ", добро пожаловать!")

inputUser = input("Давайте поработаем? (Y/N)")
if inputUser == 'y':
    print("Список возможностей:")
    print("  [1] - вывести список файлов текущей директории")
    print("  [2] - вывести информацию о системе")
    print("  [3] - показать список запущенных процессов")
    inputUser = input("Выберите возможность: ")
    if inputUser == '1':
        print("Список файлов: ", os.listdir())
    elif inputUser == '2':
        print("Текущая директория: ", os.getcwd())
        print("Операционная система: ", os.uname())
        print("Кодировка файловой системы: ", psutil.sys.getfilesystemencoding())
        print("Пользователь: ", os.getlogin())
        print("Количество процессоров: ", psutil.cpu_count())
    elif inputUser == '3':
        print("Список процессов: ", psutil.pids())
    else:
        print("Неверный ввод")
elif inputUser == 'n':
    print("До новых встреч")
else:
    print("Неверный ввод")