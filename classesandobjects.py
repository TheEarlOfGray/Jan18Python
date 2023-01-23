# Create the class using the 'class' keyword, include an init method and a repr method
class Person():
    # the init method takes in parameters like name and age and creates attributes to match on the object being created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # the repr method gives python something useful to print when you try to print out an entire object
    def __repr__(self):
        return f"{self.name}: {self.age}."

    # this is a simple method, showing that you can put into a method anything you would normally put into a function
    def printName(self):
        return f"{self.name}"

# create an object of type Person
dave = Person("Dave", 40)
# and another
john = Person("John", 50)

# printing attributes directly
print(dave.name)
print(dave.age)

print(john.name)
print(john.age)

# printing the whole object, fed by the repr method
print(dave)
print(john)

# the only way to delete an attribute already set on an object
delattr(dave, "name")
print(dave)

# check whether an object has a particular attribute, will return True if it does or False if not
print(hasattr(dave, "name"))

# gets an attribute from an object
print(getattr(dave, "name"))

# changes the value of an attribute stored in an object
setattr(dave, "name", "Simon")