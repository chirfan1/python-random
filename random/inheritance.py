class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hallo, {self.name}")

p1 = person("xaxaxa", 13)

p1.say_hello()
