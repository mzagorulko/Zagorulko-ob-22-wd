def capitalize_first_letters(first_string, second_string):
    return f"Заглавная буква 1-ой строки - {first_string.capitalize()[0]}, заглавная буква 2-ой строки - {second_string.capitalize()[0]}"


print(capitalize_first_letters(str(input("Введите строку №1 - ")), str(input("Введите строку №2 - "))))
