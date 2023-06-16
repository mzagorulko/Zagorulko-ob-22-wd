try:
    numbers = input("Введите список целых чисел через запятую: ")
    user_list = numbers.split(",")
    user_number_list = [int(x) for x in user_list]
    user_number_list.sort()
    print("Минимальное число в списке: " + str(user_number_list[0]))

except ValueError:
    print("Ошибка. Введены не целые числа")