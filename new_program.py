import os
import psutil
import sys
import shutil

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
            for i in range(0, len(file_list), 1): #Получаем список файлов и папкок
                if os.path.isfile(file_list[i]): #Проверяем, что это файл
                    new_name_file = file_list[i] + ".dupl" #Формируем новое имя
                    shutil.copy(file_list[i], new_name_file) #Копируем
        else:
            print("Неверный ввод")
elif inputUser == 'n' or inputUser == 'q':
    print("До новых встреч")
else:
    print("Неверный ввод")