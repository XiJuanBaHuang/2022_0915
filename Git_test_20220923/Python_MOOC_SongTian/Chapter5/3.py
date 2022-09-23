
def fact(n):
    if n == 0:
        return 1
    else:
        return n* fact(n - 1)


print(fact(10))

print(fact(5))


def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


count = 0
def Hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        Hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        Hanoi(n-1, mid, dst, src)

Hanoi(4, "A", "C", "B")
print(count)