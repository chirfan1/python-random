# Itteration/List(?) many value and each word
myitter = {"banana", "apple"}

x = iter(myitter)

print(next(x))
print(next(x))

print()

mystr = "string"

y = iter(mystr)

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

print()

for z in y:
    print(z)