# def taxCalc(salary):
#     tinyTax = 0
#     smallTax = 0
#     mediumTax = 0
#     largeTax = 0

#     if salary <= 12570:
#         return f"The salary of {salary} requires zero tax payment."

#     if salary > 12570:
#         tinyTax = (salary - 12570) * 0.19

#     if salary > 23000:
#         smallTax = (salary - 23000) * 0.3

#     if salary > 40000:
#         mediumTax = (salary - 40000) * 0.41

#     if salary > 150000:
#         largeTax = (salary - 150000) * 0.46

#     taxResult = tinyTax + smallTax + mediumTax + largeTax

#     return(f"The total tax paid on: {salary} is: {taxResult}.")


# salary = int(input("Please enter your salary: "))

# print(taxCalc(salary))


# This is Reece's solution

def getIncomeTaxComplex(salary):
    smallTax = 0
    mediumTax = 0
    largeTax = 0

    # 0 - 18500 is not taxed 
    # Leftover between 18500 and 34500 is taxed at 20% - need to work out how much of pay is between these values
    # leftover between 34501 and 150000 taxed at 40% - need to work out pay is between these values
    # Any money leftover is taxed at 45%

    if salary < 18500:
        return f"{salary} less than allowance, no tax paid "
    
    if salary >= 18500:
        smallTax = (salary - 18500) * 0.2

    if salary > 34500: 
        mediumTax = (salary - 34500) * 0.4

    if salary > 150000:
        largeTax = (salary - 150000) * 0.45

    finalTax = smallTax + mediumTax + largeTax
    print (f"{salary} has total tax of {finalTax}, take home money is {salary - finalTax}")

    
  

getIncomeTaxComplex(175000)