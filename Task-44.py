try:
    my_file = open('test.txt', 'r', encoding='utf-8')
    content = my_file.read()
    my_file.close()

    print(content)
except FileNotFoundError:
    print("Файл не найден")
