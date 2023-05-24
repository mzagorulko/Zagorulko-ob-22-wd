import random

my_array = []

while len(my_array) < 10:
    my_array.append(random.randint(1, 10))

print(my_array)

if my_array.count(int(input("Введите искомое число "))) == 0:
    print("Число не найдено в массиве")
else:
    print("Число найдено в массиве")
