#
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("------执行结束------")



# TextProBarV1.py
for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.01)
print()


# TextProBarV3.py
scale3 = 50
print("执行开始".center(scale3//2, "-"))
start = time.perf_counter()
for i in range(scale3+1):
    a = '*' * i
    b = '.' * (scale3-i)
    c = (i/scale3) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n" + "执行结束".center(scale3//2, '-'))
