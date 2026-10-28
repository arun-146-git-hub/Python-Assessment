""" Classify student performance by marks. """

students = {"Rahul": 85, "Amit": 35, "Priya": 72, "Neha": 48}

for name, marks in students.items():
    if marks >= 80:
        category = "Excellent"
    elif marks >= 60:
        category = "Good"
    elif marks >= 40:
        category = "Average"
    else:
        category = "Fail"
    print(name, category)
