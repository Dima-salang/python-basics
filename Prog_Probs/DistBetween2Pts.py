from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculate_distance(point1, point2):
    return sqrt(((point2.x - point1.x) + (point2.y - point1.y)))


first_point = Point(0, 1)
sec_point = Point(2, 3)
print(calculate_distance(first_point, sec_point))