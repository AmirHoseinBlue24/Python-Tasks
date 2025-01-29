def triangle_area(base, height):
    area = 0.5 * base * height
    return area

base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = triangle_area(base, height)
print(f"area is: {area}")
