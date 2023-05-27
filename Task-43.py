try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    division_result = a / b
    print(f"Результат деления: {division_result}")
except ValueError:
    print("Ошибка. Проверьте, что вы ввели числа. ")
except ZeroDivisionError:
    print("Ошибка. Деление на 0 невозможно.")
