import random


def get_random_array():
    random_array = []
    while len(random_array) < 10:
        random_array.append(random.randint(1, 10))
    return random_array


my_array = get_random_array()
print(sum(my_array))
