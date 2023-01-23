
# accessing the csv file and reading in all of the data as a list of strings
with open("carSale.csv", "r") as file1:
    lines = file1.readlines()

# splitting the strings in that list into sub-lists [[one sub-list][another sub-list][etc]]
for line in lines:
    lines[lines.index(line)] = line.split(",")

# removing the first sub-list (the months) and creating a single unigue list with the months in it
months = lines.pop(0)

# This code just strips out the \n from any string in the months list
for month in months:
    if "\n" in month:
        months[months.index(month)] = month[0:3]

# this code converts all of the items in each of the remaining sub-lists into integers except the first item in each sub-list (the company name)
for line in lines:
    for lin in line:
        if line.index(lin) == 0:
            pass
        else:
            line[line.index(lin)] = int(lin)


## This code if uncommented would split the first item in each sub-list apart into a single uniqu list of company names
# company = []

# for indItem in lines:
#     company.append(indItem.pop(0))
    
# print(company)

print(months)
print(lines)



# this code splits the list of sub-lists into a dictionary, with the first item in each sub-list being the key and the remaining items in the sub-list being the value
dict1 = {}
for listItem in lines:
    dict1[listItem[0]] = listItem[1:] # Here I have used list 'slicing'.
print(dict1)


# this code looks for an item in the dictionary that has the given key, and if found, works out the total of the corresponding list value 
for item in dict1.keys():
    if item == "Ford Motor Company":
        result = sum(dict1[item])
print(result)


# this code looks through the values stored in the dictionary, matching the amounts stored in that list with the index position of the month "May", totalling all of the integers found
result2 = 0
for item in dict1.keys():
    result2 += dict1[item][months.index("May")]
print(result2)


# this finds all of the dict-value-lists items that match the month "Aug" similar to the previous code and then averages the result
result3 = 0
for item in dict1.keys():
    result3 += dict1[item][months.index("Aug")]
result3 = result3 / len(dict1.keys())
print(result3)

# this code totals the first four of the numbers in each dict-value-list and stores them in a list
janApr = []
for item in dict1.keys():
    janApr.append(sum(dict1[item][:4]))


# this code turns that list into a dictionary, matching the company to the 'total over 4 months' that it applies to 
dict2 = {}
control = 0
for key in dict1:
    dict2[key] = janApr[control]
    control += 1
print(dict2)

# this code totals up all of the items at each index position in the dict-value-lists, so all the items at index position 0 added together then all the items at index position 1 etc.
# these totals are then stored in a list that matches by order, the list of months. We then use the max() function to work out which month was the most and use the index position to find out which month it matches.
totals = []
for month in range(len(months)):
    temp = 0
    for item in dict1.keys():
        temp += dict1[item][month]
    totals.append(temp)
control = totals.index(max(totals))
result4 = months[control]
print(result4)
