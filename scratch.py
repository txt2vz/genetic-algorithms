from collections import namedtuple


Thing = namedtuple('Thingx', ['name', 'value', 'weight'])

first_example = [
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192),
]

Point = namedtuple("Point", "x y")

poiny = Point(2,3)

print (poiny.y)

print(Thing[1])

z = namedtuple("word", ["wrd", "len", "freq"])

mf = z('om', 2,323)

print (mf)
print (mf.len)


def generate_things(num: int) -> [Thing]:
    return [Thing(f"thing{i}", i, i) for i in range(1, num+1)]

cnt = generate_things(3)
print(f"cnt {cnt}  cnt1  {cnt[1].name} cnt1 weight {cnt[1].weight} ")