class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hallo {self.name}, {self.age}"


p1 = person("xaxaxa", 24)

print(p1)