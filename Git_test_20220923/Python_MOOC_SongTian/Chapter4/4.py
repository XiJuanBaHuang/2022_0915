import random
#random.seed(10)
print(random.random())
print(random.randint(10, 100))
print(random.randrange(10, 100, 10))
print(random.getrandbits(16))
print()
print(random.uniform(10, 100))
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(s))
print(random.choices(s))
random.shuffle(s)
print(s)