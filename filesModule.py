# with open("example.txt", "r") as file1:
#     var1 = file1.read()

# var2 = var1.split(",")

# print(var2)

# with open("example.txt", "r") as file1:
#     var1 = file1.readline()
#     var2 = file1.readline()
#     file1.seek(0)
#     var3 = file1.readline()

# print(var1)
# print(var2)
# print(var3)



# with open("example.txt", "r") as file1:
#     var1 = file1.readlines()

# for line in var1:
#     print(line)

# print(var1)

with open("example.txt", "r") as file1:
    contents = file1.readlines()

with open("example.txt", "w") as file1:
    for line in contents:
        file1.write(line)
    file1.write("\nThis is an extra line.")