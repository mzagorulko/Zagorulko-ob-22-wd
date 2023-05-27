my_file = open('text.txt', 'r', encoding='utf-8')
content = my_file.read()
my_file.close()

print(content)
