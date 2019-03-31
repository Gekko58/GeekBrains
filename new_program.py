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
    inputUser = int(input("Выберите возможность: "))
    if inputUser == 1:
        print(os.listdir())
    elif inputUser == 2:
        pass
    elif inputUser == 3:
        print(psutil.pids())
    else:
        print("Неверный ввод")
elif inputUser == 'n':
    print("До новых встреч")
else:
    print("Неверный ввод")