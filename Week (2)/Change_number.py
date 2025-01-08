def change(a,b):
    a = a+b
    b = a-b
    a = a-b
    
    print(f'Number changed, number one is: {a} number two is: {b}')

a = int(input("First number: "))
b = int(input("Secoand number: "))
change(a, b)