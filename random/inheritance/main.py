class itteration:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a *= 2
        return x

myclass = itteration()
myitter = iter(myclass)

print(next(myitter))
print(next(myitter))
print(next(myitter))

