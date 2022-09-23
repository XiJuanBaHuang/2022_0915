#string_operations

s = '''Python
                语言'''
print(s)
print()

s1 = "〇一二三四五六七八九十"
print(s1[0:])
print(s1[:3])
print(s1[1:8:2])
print(s1[::-1])
print(s1[::1])

# WeekNamePrintV1.py
# weekStr = "星期一星期二星期三星期四星期五星期六星期日"
# weekID = eval(input("请输入星期数字(1-7):\n"))
# pos = (weekID - 1) * 3
# print(weekStr[pos: pos+3])

# WeekNamePrintV2.py
# weekStr = "一二三四五六日"
# weekID = eval(input("请输入星期数字(1-7):\n"))
# print("星期" + weekStr[weekID-1])

s2 = "一二三456"
print(len(s2))

print("1 + 1 = 2" + chr(10004))
print(chr(9801))
print(ord("♉"))
print("这个字符♉的Unicode值是:" + str(ord("♉")))
for i in range(12) :
    print(chr(9800 + i), end = "")
print()

s3 = "ABVGFUYJFFCTuhdwuytfugiGYUDFHGtf"
print(s3.lower())
print(s3.upper())
print()


s4 = "k, d,KO,.x old, fr"
print(s4.split(","))
#split_default = " "
print()

s5 = "an apple A day"
print(s5.count("a"))
print()

s6 = "python"
print(s6.replace("n", "n123.io"))
print(s6.center(30, "-"))
print()

s7 = "= python= okok"
print(s7.strip(" =np"))

s8 = ","
s8_1 = "12345ijshuypkd.,ond"
print(s8.join("12345"))
print(s8.join(s8_1))



print("{0:=^20}".format("PYTHON"))
print("{0:*>20}".format("BIT"))
print("{:10}".format("BIT"))

print("{0:,.2f}".format(12345.6789))
# print()
print("{0:b}, {0:c}, {0:d}, {0:o}, {0:x}, {0:X}".format(425))
print("{0:e}, {0:E}, {0:f}, {0:%}".format(3.14))


print(1//2)