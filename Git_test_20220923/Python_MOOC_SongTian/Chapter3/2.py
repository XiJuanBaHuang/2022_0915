#DayDayUp.py

print(pow(1.01, 365))
print(pow(0.99, 365))
print()

####################################Q11111111111111
dayup1 = pow(1.001, 365)
daydown1 = pow(0.999, 365)
print("向上: {:.2f}, 向下: {:.2f}".format(dayup1, daydown1))
print()

####################################Q22222222222222
dayfactor = 0.01
dayup2 = pow(1+dayfactor, 365)
daydown2 = pow(1-dayfactor, 365)
print("向上: {:.2f}, 向下: {:.2f}".format(dayup2, daydown2))
print()

######################################Q333333333333
dayup3 = 1.0
dayfactor3 = 0.01
for i in range(365):
    if i % 7 in[6, 0]:
        dayup3 = dayup3 * (1 - dayfactor3)
    else:
        dayup3 = dayup3 * (1 + dayfactor3)
print("工作日的力量: {:.2f}".format(dayup3))
print()

########################################Q4444444444
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor4 = 0.01
while dayUP(dayfactor4) < 37.78:
    dayfactor4 += 0.001
print("工作日的努力参数:{:.3f}".format(dayfactor4))

########################################Q55555555555
