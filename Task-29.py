def reverse_string(initial_string):
    temp_list = list(initial_string)
    temp_list.reverse()
    return ''.join(temp_list)


result_string = reverse_string(str(input("Введите строку для реверса: ")))
print(result_string)
