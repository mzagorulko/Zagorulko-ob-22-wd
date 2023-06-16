try:
    number = int(input("Введите целое число: "))
    summ = 0
    for i in range(1, number + 1):
        summ += i
    print("Сумма: " + str(summ))

except ValueError:
    print("Ошибка. Введено не целое число")