print("Это моя первая программа")
print("Привет программист!")

name = input("Введите ваше имя: ")
print(name, ", добро пожаловать!")

inputUser = input("Давайте поработаем? (Y/N)")
if inputUser == 'y':
    print("Это хорошо")
elif inputUser == 'n':
    print("До новых встреч")
else:
    print("Неверный ввод")