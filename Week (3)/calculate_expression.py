def calculate_expression(x):
    y = ((x << 5) - x) - ((x << 4) + x) + 5
    return y

x = int(input("Enter the value of x: "))

print("Result:", calculate_expression(x))
