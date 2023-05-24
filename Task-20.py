import random


def get_random_array():
    random_array = []
    while len(random_array) < 10:
        random_array.append(random.randint(1, 100))
    print(random_array)


get_random_array()
