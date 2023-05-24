def symbols_count(initial_string):
    result = {}
    unique_characters = set(initial_string)
    for i in unique_characters:
        result[i] = initial_string.count(i)
    return result


print(symbols_count(str(input("Введите строку для подсчета символов: "))))