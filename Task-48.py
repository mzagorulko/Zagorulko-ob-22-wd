import numpy


def average_in_array(initial_array, k):
    print(numpy.mean(list(filter(lambda x: x > k, initial_array))))


average_in_array([5, 7, 11, 13, 20, 25], 10)
