from math import gcd
from functools import reduce

list1 = [24, 36, 48, 60]
list2 = [12, 18, 24, 36, 72]


def array_gcd(initial_list):
    print(reduce(gcd, initial_list))


list1.extend(list2)
array_gcd(list1)
