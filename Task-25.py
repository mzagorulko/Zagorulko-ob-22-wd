def is_number_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True


user_input = int(input("Введите число для проверки: "))
if is_number_prime(user_input):
    print("Число простое")
else:
    print("Число не простое")

