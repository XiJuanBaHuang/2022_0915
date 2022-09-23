def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(fact(10) / fact(5))


def fact2(n, m=1):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s // m


print(fact2(10, 5))
print(fact2(m=5, n=10))


def fact3(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s


print(fact3(10, 3))
print(fact3(10, 3, 5, 8))


def fact2_1(n, m=1):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s // m, n, m


print(fact2_1(10, 5))
a, b, c = fact2_1(10, 5)
print(a, b, c)
t = [1, 2, 3]
a, b, c = t
print(a, b, c)

n, s = 10, 100


def fact4(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(fact4(n), s)


def fact4_1(n):
    global s
    for i in range(1, n + 1):
        s *= i
    return s


print(fact4_1(n), s)

ls = ['F', 'f']


def func(a):
    # ls = []
    ls.append(a)
    return


func('C')
print(ls)


f = lambda x, y : x + y
print(f(10, 15))
