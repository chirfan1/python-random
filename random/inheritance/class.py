class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(ni):
        print(ni.name, ni.age)

class emp(person):
    def __init__(self, name, age):
        super().__init__(name, age)

        
    def say_hello(ni):
        super().say_hello()
        print("Gabungan person dan emp", ni.name, ni.age)
        print(f"Ini Class Emp {ni.name}, {ni.age}")

p1 = person("xaxaxa", 24)
e1 = emp("vasv", 212)

print(p1.name)
print(p1.age)
p1.say_hello()

print("")
print(e1.name)
print(e1.age)
e1.say_hello()