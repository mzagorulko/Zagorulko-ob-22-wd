try:
    a = int(input("Введите число: "))
    square = pow(a, 2)
    print(f"Результат возведения в квадрат: {square}")
except ValueError:
    print("Ошибка. Проверьте, что вы ввели числа. ")