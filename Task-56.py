import os.path
from sys import argv

script, file_name = argv
if not os.path.isfile(file_name):
    raise ValueError("Файл отсутствует")

initial_file = open(file_name, 'r')
text = initial_file.read()
initial_file.close()

service_symbols = ['.', ':', ',', '!', '-', '—', '"', "'", '(', ')', '?', '_', '`', '=', '[', ']']
words_list = []
for word in text.lower().split():
    if word not in service_symbols:
        located_word = word
        if word[-1] in service_symbols:
            located_word = located_word[:-1]
        if word[0] in service_symbols:
            located_word = located_word[1:]
        words_list.append(located_word)

located_dictionary = dict()
for word in words_list:
    located_dictionary[word] = located_dictionary.get(word, 0) + 1

located_count = []
for key, value in located_dictionary.items():
    located_count.append((value, key))
    located_count.sort(reverse=True)

print("самое часто встречающееся слово в файле: " + located_count[0][1])
