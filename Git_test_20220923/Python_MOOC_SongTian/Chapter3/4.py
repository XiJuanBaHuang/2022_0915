# time package
import time
print(time.time())
print(time.ctime())
print(time.gmtime())

t = time.gmtime()
# time.strftime("%Y-%m-%d %H:%M:%S", t)
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
print(time.strftime("%Y-%B-%d %H:%M:%S", t))
print(time.strftime("%Y-%b-%d %H:%M:%S", t))

print(time.strftime("%Y-%m-%d %a %H:%M:%S", t))
print(time.strftime("%Y-%m-%d %A %H:%M:%S", t))




start = time.perf_counter()
end = time.perf_counter()
print(end - start)
def wait():
    time.sleep(3)
wait()