# Написать программу, которая принимает на вход строку и выводит на экран количество различных
# подстрок строки, начинающихся и заканчивающихся одним и тем же символом.
import string

user_string = str(input("Введите строку для анализа: "))
result_substrings = []

# Убираем пунктуацию из строки
clear_string = user_string.translate(str.maketrans('', '', string.punctuation))

# Разбиваем строку на список подстрок
substrings = clear_string.split()

# Проходим по всем подстрокам и сверяем первый и последний символ подстроки
for substring in substrings:
    if substring.endswith(substring[0]):
        result_substrings.append(substring)

# Анализируем и выводим результат
if len(result_substrings):
    print(f"Подстроки, начинающиеся и заканчивающиеся одинаковыми символами:")
    print(*result_substrings, sep='\n')
else:
    print("В строке нет подстрок, которые бы начинались и заканчивались одинаковым символом")
