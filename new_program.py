import os
import psutil
import sys
import shutil

def duplicate_file(file_list): #Функция содаёт дубликаты файлов
    for i in file_list:  # Получаем список файлов и папкок
        if os.path.isfile(i):  # Проверяем, что это файл
            new_name_file = i + ".dupl"  # Формируем новое имя
            shutil.copy(i, new_name_file)  # Копируем
            if os.path.exists(new_name_file):
                print("Файл", new_name_file, "успешно создан")
            else:
                print("Не могу создать файл или это папка")
        else:
            print("Неверное имя файла")

def delete_dublicate(name_folder): #Функция удаляет дубликаты файлов из указанной директории
    if os.path.isdir(name_folder):
        number_del_file = 0
        file_list = os.listdir(name_folder)
        for i in file_list:
            full_name = os.path.join(name_dir, i)
            if i.endswith(".dupl"):
                os.remove(full_name)
                if not os.path.exists(full_name):
                    number_del_file += 1
                    print("Файл", full_name, "успешно удалён")
                else:
                    print("Невозможно удалить файл")
        return "Количество удалённых файлов: " + str(number_del_file)
    else:
        return "Не верно указана директория"

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
            answer_string = delete_dublicate(name_dir)
            print(answer_string)
        else:
            print("Неверный ввод")
elif inputUser == 'n' or inputUser == 'q':
    print("До новых встреч")
else:
    print("Неверный ввод")