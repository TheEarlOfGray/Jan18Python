# fruitFile = open("fruit.txt", "r") 

# data = fruitFile.readline() 

# print(data) 

# fruitFile.close() 

# listFruit = data.split(",")

# for fruit in listFruit:
#     print(fruit)

# fruitFile = open("fruit.txt", "a") 

# fruitFile.write(",kiwi") 

# fruitFile.close() 

with open("numbers.txt", "w") as file1:
    for num in range(1, 11):
        content = str(num) + "\n"
        file1.write(content)