with open("carSale.csv", "r") as file1:
    lines = file1.readlines()

for line in lines:
    lines[lines.index(line)] = line.split(",")

months = lines.pop(0)

for month in months:
    if "\n" in month:
        months[months.index(month)] = month[0:3]

for line in lines:
    for lin in line:
        if line.index(lin) == 0:
            pass
        else:
            line[line.index(lin)] = int(lin)



# company = []

# for indItem in lines:
#     company.append(indItem.pop(0))
    
# print(company)

print(months)
print(lines)



dict1 = {}

for listItem in lines:
    dict1[listItem[0]] = listItem[1:] # Here I have used list 'slicing'.

print(dict1)

for item in dict1.keys():
    if item == "Ford Motor Company":
        result = sum(dict1[item])

print(result)


result2 = 0

for item in dict1.keys():
    result2 += dict1[item][months.index("May")]

print(result2)

result3 = 0

for item in dict1.keys():
    result3 += dict1[item][months.index("Aug")]

result3 = result3 / len(dict1.keys())
print(result3)

