def sum_reverse(a):
    c = [int(b) for b in a]
    
    r = list(reversed(c))
    s = sum(c)

    print(f'Reverse is: {r} and sum is: {s}')

n = input("Enter numbers: ")

sum_reverse(n)
