import math

def calculate_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def calculate_surface_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area


radius = float(input("radius of sphere: "))
volume = calculate_volume(radius)
surface_area = calculate_surface_area(radius)
print(f"volume is: {volume}")
print(f"surface area is: {surface_area}")

