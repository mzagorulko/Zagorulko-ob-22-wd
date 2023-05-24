def lcm(a, b):
    m = a * b
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    print(f"Наименьший общий множитель - {m // a + b}")


lcm(int(input("Число №1 - ")), int(input("Число №2 - ")))
