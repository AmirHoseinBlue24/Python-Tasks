def calculator(a,b):
    Salary = a*b
    print(f'Salary is {Salary - (10 // 10)*100}')

a = float(input("Salary per hour: "))
b = float(input("Hour: "))

calculator(a, b)