def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

number = float(input("Enter a number: "))

square, cube = calculate_square_and_cube(number)

print(f"The square of {number} is: {square}")
print(f"The cube of {number} is: {cube}")
