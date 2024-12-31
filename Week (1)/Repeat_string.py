def string_repeat(s,r):
    for i in range(r):
        print(s, end=" ")

string = str(input("Enter a string: "))
repeat = int(input("Enter repeat: "))

string_repeat(string, repeat)
