def sum_reverse(a):

    c = a%10
    b = int(a/10)
    print(f'Sum is: {c+b}')
    print(f'Reverse is: {b,c}')
    
    


n = int(input("Enter numbers: "))

sum_reverse(n)
