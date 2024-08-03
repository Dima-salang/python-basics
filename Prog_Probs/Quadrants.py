class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_quadrant(point):
    if point.x > 0 and point.y > 0:
        return "Quadrant I"
    elif point.x < 0 < point.y:
        return "Quadrant II"
    elif point.x < 0 and point.y < 0:
        return "Quadrant III"
    elif point.x > 0 > point.y:
        return "Quadrant IV"
    elif point.x == 0 and (point.y > 0 or point.y < 0):
        return "Y-Axis"
    elif point.y == 0 and (point.x > 0 or point.x < 0):
        return "X-Axis"
    elif point.x == 0 and point.y == 0:
        return "Origin"
    else:
        return "Not a valid point"


point1 = Point(12, 15)
point2 = Point(0, 0)
print(get_quadrant(point1))
print(get_quadrant(point2))



