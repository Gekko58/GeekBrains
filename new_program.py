import os
import psutil
import sys
import shutil

def duplicate_file(file_list):
    for i in file_list:  # Получаем список файлов и папкок
        if os.path.isfile(i):  # Проверяем, что это файл
            new_name_file = i + ".dupl"  # Формируем новое имя
            shutil.copy(i, new_name_file)  # Копируем
        else:
            print("Неверное имя файла")

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
        print("  [4] - дублирование файлов в текущей директории")
        print("  [5] - копирование указанного файла")
        print("  [6] - удалить дубликаты файлов в указанной директории")
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
        elif inputUser == '4':
            file_list = os.listdir()
            duplicate_file(file_list)
        elif inputUser == '5':
            file_list = input("Введите имя файла: ").split() #Получаем имя файла от пользователя
            duplicate_file(file_list)
        elif inputUser == '6':
            name_dir = input("Введите имя директории: ")
            if os.path.isdir(name_dir):
                file_list = os.listdir(name_dir)
                for i in range(0, len(file_list), 1):
                    full_name = os.path.join(name_dir, file_list[i])
                    if full_name.endswith(".dupl"):
                        os.remove(full_name)
            else:
                print("Нет такой директории")
        else:
            print("Неверный ввод")
elif inputUser == 'n' or inputUser == 'q':
    print("До новых встреч")
else:
    print("Неверный ввод")