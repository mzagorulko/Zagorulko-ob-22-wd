try:
    user_file = open(str(input("Введите имя файла, который вы хотите посмотреть: ")), 'r', encoding='utf-8')
    content = user_file.read()
    user_file.close()

    print(content)
except FileNotFoundError:
    print("Ошибка. Файл не найден")
except IOError:
    print("Ошибка чтения файла")
