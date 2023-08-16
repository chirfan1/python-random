class itteration:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a *= 2
            return x
        else:
            raise StopIteration

myclass = itteration()
myitter = iter(myclass)

for x in myitter:
    print(x)

