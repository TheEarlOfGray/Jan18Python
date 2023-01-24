class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} {self.age}"
        

import sqlite3

conn = sqlite3.connect("otherexample")

cursor = conn.cursor()

# cursor.executescript("CREATE TABLE example (excol VARCHAR(30));")

# cursor.executescript("INSERT INTO example (excol) VALUES ('random'),('text'),('goes'),('here');")

# retrieved = cursor.execute("SELECT * FROM example").fetchall()

# for item in retrieved:
#     print(item)

# cursor.executescript("DROP TABLE example;")

# with open("create.sql", "r") as file1:
#     createString = file1.read()

# cursor.executescript(createString)

with open("SQLQuery1.sql", "r") as file1:
    createString = file1.read()

list1 = cursor.execute(createString).fetchall()

list2 = []

for item in list1:
    execStr = f"{item[0]} = Person(f\"{item[0] + ' ' + item[1]}\", item[2])"
    exec(execStr)
    list2.append(f"{item[0]}")

print(Sally)
print(Dave)
print(Simon)
print(Fiona)

# dict1 = {}
# for item in list1:
#     dict1[item[0]+" "+item[1]] = item[2]

# print(dict1)