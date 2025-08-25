def isHappynumber(n):
    num = n
    x = n

    while num > 9:
        num = 0
        while x > 0:
            d = x % 10
            num += d * d
            x = int(x / 10)
        x = num
    if num == 1 or num == 7:
        return True
    else:
        return False

num = 19

if isHappynumber(num):
    print(f'{num} is Happy Number')
else:
    print("isn't i'm sorry")