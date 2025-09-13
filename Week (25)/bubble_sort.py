def bubble(lst):
    n = len(lst)-1
    for j in range(0, n):
        for i in range(0, n-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)

bubble([5, 6, 2, 1])