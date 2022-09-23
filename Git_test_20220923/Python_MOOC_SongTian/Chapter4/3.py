# for i in range()
# while

# for i in range(N):
for i in range(5):
    print("Hello:", i)

# for i in range(M, N):
for i in range(1, 6):
    print(i)

# for i in range(M, N, K):
for i in range(1, 6, 2):
    print("Hello:", i)

# for c in string:
for c in "Python123":
    print(c, end=",")
print()

# for item in ls:
for item in [123, "PY", 456]:
    print(item, end=",")
print()

# for line in fi:





a = 3
while a >0 :
    a -= 1
    print(a)

# break continue
for c in "PYTHON":
    if c == 'T':
        continue
    print(c, end="")
print()

for c in "PYTHON":
    if c == 'T':
        break
    print(c, end="")
print()



s = "PYTHON"
while s != "" :
    for c in s :
        print(c, end="")
    print()
    s = s[:-1]

s = "PYTHON"
while s != "" :
    for c in s :
        if c == 'T' :
            break
        print(c, end="")
    print()
    s = s[:-1]



# break else
# no break, then do else
for c in "PYTHON" :
    if c == "T" :
        continue
    print(c, end="")
else:
    print("\nAll Right.")

for c in "PYTHON" :
    if c == "T" :
        break
    print(c, end="")
else:
    print("All Right.")

print()
print()
for page in range(2, 42):
    print('http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_ ' + str(page) + '.shtml')