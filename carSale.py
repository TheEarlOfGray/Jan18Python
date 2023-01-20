with open("carSale.csv", "r") as file1:
    lines = file1.readlines()

for line in lines:
    lines[lines.index(line)] = line.split(",")



months = lines.pop(0)



for line in lines:
    for lin in line:
        if line.index(lin) == 0:
            pass
        else:
            line[line.index(lin)] = int(lin)

print(months)
print(lines)

dict1 = {"Ford Motor Company": [16629, 10390, 40755, 18074, 19892, 22049, 17049, 10764]}
print(sum(dict1["Ford Motor Company"]))