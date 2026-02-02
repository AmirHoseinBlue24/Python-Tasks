f = lambda n : n*2
print(f(5))


f1 = lambda i,n : i+n
print(f1(3,7))


f2 = lambda n : n%2
print(f2(4))


f3 = lambda i, n: (i+n,i-n)
print(f3(8, 3))


f4 = lambda n : n ** 2
print(f4(6))


print(list(map(str.upper, ["apple", "banana"])))


print(list(map(len, ['Ali', ' Reza'])))


m = map(lambda i, n: i+n, [1, 2, 3], [4, 5, 6])
print(list(m))


m1 = map(str, [1, 2,3])
print(list(m1))


m2 = map(lambda i : i > 10, [5, 7, 12, 15])
print(list(m2))


l = filter(lambda i : i > 10, [5, 7, 12, 15])
print(list(l))


l1 = filter(None, [0, '', None, 5, 'hello'])
print(list(l1))


func = lambda n: not n%2
l2 = filter(func, [1, 2, 3, 4, 5, 6])
print(list(l2))


l3 = filter(lambda n : len(n)<5, ['apple', 'bot', 'cat', 'doggy'])
print(list(l3))

import functools as f

r = f.reduce(lambda i,n : i+n, [1, 2, 3, 4])
print(r)


r1 = f.reduce(lambda i,n : i*n, [1, 2, 3, 4])
print(r1)


r3 = f.reduce(max, [5, 9, 2, 8])
print(r3)


r4 = f.reduce(min, [5, 9, 2, 8])
print(r4)


r5 = f.reduce(lambda n, i : n+i, ['Python', 'is', 'fun'])
print(r5)


s = sorted([4, 2, 5, 1], reverse=False)
print(s)


s = sorted([4, 2, 5, 1], reverse=True)
print(s)


import operator as o
lst = [{'Name':'Ali', 'Score':12}, {'Name':'Ali', 'Score':9}]
s = sorted(lst, key=o.itemgetter('Score'))
print(s)


lst = [(1,'a',10), (2,'b',5)]
s1 = sorted(lst, key=o.itemgetter(2))
print(s1)


d = {'Ali':13, 'Sara':17, 'Taha':15}
s2 = sorted(d.items(), key=lambda x: x[1])
print(s2)