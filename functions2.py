def greet(name, greet="Hello"):
    return f"{greet} {name}"

print(greet("Dave", "Hi"))
print(greet(greet="Hola", name="Dave"))
print(greet("Dave"))