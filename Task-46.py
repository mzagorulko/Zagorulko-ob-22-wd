try:
    with open('test.txt', 'w') as file:
        file.write('Hello, world!')
except FileNotFoundError:
    print("Ошибка. Файл не найден.")
except IOError:
    print("Ошибка записи в файл")
