import math

coordinate_list = [(1, 2), (3, 4), (-1, 5), (6, -3)]


def sort_by_distance(coordinates):
    return math.dist(coordinates, (0, 0))


sorted_list = sorted(coordinate_list, key=sort_by_distance)

print("Отсортировать по расстоянию от начала координат: ", sorted_list)
