def func1(name):
    return name.upper()


def addgreet(name):
    return f"Hello {name}"


print(func1("Dave"))
print(func1("John"))
print(addgreet("Simon"))
print(addgreet("Steve"))
print(addgreet(func1("Phil")))

var1 = f"hello {func1('simon')}"
print(var1)