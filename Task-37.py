import random


def fill_dummy():
    dummy = []
    while len(dummy) < 10:
        dummy.append(random.randint(1, 100))
    print(f"Массив для поиска 2-х минимальных значений - {dummy}")
    return dummy


def get_minimal_couple(initial_list):
    return sorted(initial_list)[0:2]


print(f"Минимальные значения в массиве - {get_minimal_couple(fill_dummy())}")
