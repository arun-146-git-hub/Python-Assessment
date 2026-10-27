""" Check loan eligibility by age, salary and credit score. """

age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))

if age >= 21:
    if salary >= 25000:
        if credit_score >= 750:
            print("Loan approved")
        elif credit_score >= 650:
            print("Loan approved with higher interest")
        else:
            print("Loan rejected")
    else:
        print("Salary is too low")
else:
    print("Age requirement not met")
