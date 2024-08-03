from collections import namedtuple

Point = namedtuple("point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)