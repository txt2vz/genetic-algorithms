from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

# Create a namedtuple type, Poin
Point = namedtuple("Point", "x y")
point = Point(2, 4)
print(point)
print(point.x)

point2 = Point(7,11)
print(f"point s {point2}  point2 x {point2.x}")