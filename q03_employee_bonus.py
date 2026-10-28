""" Calculate employee bonus based on experience, salary and performance. """

experience = float(input("Enter experience in years: "))
salary = float(input("Enter salary: "))
performance = float(input("Enter performance score: "))

if experience >= 1 and salary >= 50000:
    if performance >= 90:
        bonus_rate = 0.20
    elif performance >= 75:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.05
elif salary < 50000:
    if performance >= 90:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.05
else:
    bonus_rate = 0

print("Bonus:", round(salary * bonus_rate, 2))
