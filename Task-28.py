a = int(input("a - "))
b = int(input("b - "))
operation = str(input("операция(+/-/%/*) - "))

if operation == '+':
    print(f"Сумма чисел - {a + b}")
elif operation == '-':
    print(f"Разность чисел - {a - b}")
elif operation == '%':
    print(f"Частное - {a / b}, остаток - {a % b}")
elif operation == '*':
    print(f"Произведение - {a * b}")
else:
    print("Неверная операция")
