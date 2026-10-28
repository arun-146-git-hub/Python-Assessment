""" Classify employees by salary and experience. """

employees = {
    "Rahul": {"salary": 60000, "experience": 6},
    "Amit": {"salary": 40000, "experience": 4},
    "Priya": {"salary": 70000, "experience": 3},
    "Neha": {"salary": 45000, "experience": 1}
}

for name, details in employees.items():
    salary = details["salary"]
    experience = details["experience"]

    if salary >= 50000:
        if experience >= 5:
            category = "Senior"
        else:
            category = "Mid-Level"
    else:
        if experience >= 3:
            category = "Experienced Junior"
        else:
            category = "Fresher/Junior"

    print(name, category)
