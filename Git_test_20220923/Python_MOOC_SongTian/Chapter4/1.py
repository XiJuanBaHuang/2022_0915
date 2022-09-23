# if else



# 4-1-1
guess = eval(input())
if guess == 99:
    print("Guess Right!")
else:
    print("Guess Wrong!")


guess = eval(input())
print("Guess {}!".format("Right" if guess == 99 else "Wrong"))


score = eval(input())
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
# not or and



# try except
try :
    num = eval(input())
    print(num**2)
except NameError:
    print("Error Input!")
#else bonus
#finally must be done
