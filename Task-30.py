
def count_letter_types(initial_string):
    vowels_reference = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants_reference = "бвгджзклмнпрстфхцчшщьъБВГДЖЗКЛМНПРСТФХЦЧШЩЬЪ"
    space_reference = " "
    vowels_count = 0
    consonants_count = 0
    marks_count = 0
    spaces_count = 0

    for i in initial_string:
        if i in vowels_reference:
            vowels_count += 1
        elif i in consonants_reference:
            consonants_count += 1
        elif i in space_reference:
            spaces_count += 1
        else:
            marks_count += 1
    return [vowels_count, consonants_count, marks_count, spaces_count]


letters_count = count_letter_types(str(input("Введите строку для подсчетв количества букв и символов: ")))
print(f"Гласных букв в строке - {letters_count[0]}; Согласных букв в строке - {letters_count[1]}; Знаков препинания - {letters_count[2]}; Пробелов - {letters_count[3]}")


