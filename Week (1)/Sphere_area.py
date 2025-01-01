import math

def volume(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume

def surface_area(r):
    surface_area = 4 * math.pi * (r ** 2)
    return surface_area


r = float(input("radius of sphere: "))
v = volume(r)
a = surface_area(r)
print(f"volume is: {v}")
print(f"surface area is: {a}")
