def calculate_trapezoid_area(smaller_base, larger_base, height):
    area = (smaller_base + larger_base) * height / 2
    return area

smaller_base = float(input("Enter ssmaller base: "))
larger_base = float(input("Enter larger base: "))
height = float(input("Enter height: "))

area = calculate_trapezoid_area(smaller_base, larger_base, height)

print(f"The area of the trapezoid is: {area}")