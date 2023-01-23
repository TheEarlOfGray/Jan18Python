class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}."

    def printName(self):
        return f"{self.name}"

dave = Person("Dave", 40)
john = Person("John", 50)

print(dave.name)
print(dave.age)
print(john.name)
print(john.age)
print(dave)
print(john)


delattr(dave, "name")
print(dave)