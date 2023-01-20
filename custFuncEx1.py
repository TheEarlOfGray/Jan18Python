from random import randint

def oct():
    return randint(1, 8)

def dec():
    return randint(1, 10)

print(oct())
print(dec())

def fourDice():
    results = []
    for num in range(4):
        var = randint(1, 6)
        results.append(var)

    return results

result = fourDice()

for num in result:
    print(num)


def fourDice2():
    results = []
    for num in range(4):
        var = randint(1, 6)
        results.append(var)
    print(results)
    sortedList = sorted(results)
    sortedList.pop(0)
    print(sortedList)
    return sum(sortedList)

def custDie(num):
    return randint(1, num)

var1 = fourDice2()
print(var1)

for i in range(6):
    print(custDie(var1))