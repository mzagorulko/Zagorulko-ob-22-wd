import random


def fill_dummy(array_length):
    dummy = []
    while len(dummy) < array_length:
        dummy.append(random.randint(1, 100))
    print(f"Массив для поиска четных чисео - {dummy}")
    return dummy


def get_evens(random_list):
    evens = []
    for i in range(len(random_list)):
        if (random_list[i] % 2) == 0:
            evens.append(random_list[i])
    return evens


print(f"Четные числа в массиве - {get_evens(fill_dummy(int(input('Введите размерность массива: '))))}")


