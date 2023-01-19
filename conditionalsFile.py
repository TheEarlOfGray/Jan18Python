score = int(input("Enter the score: "))
grade = "Ungraded"
level = int(input("Would you like level 1 or level 2? "))

if level == 1:
    level = True
else:
    level = False


if level:
    if score >= 0 and score <= 100:
        if score >= 70:
            grade = "Distiction"
        elif score >= 60:
            grade = "Merit"
        elif score >= 50:
            grade = "Pass"
        else:
            grade = "Fail!!!!"
    else:
        print("That is not a valid number!!")
else:
    if score >= 0 and score <= 100:
        if score >= 60:
            grade = "Distiction"
        elif score >= 50:
            grade = "Merit"
        elif score >= 40:
            grade = "Pass"
        else:
            grade = "Fail!!!!"
    else:
        print("That is not a valid number!!")

print(grade)