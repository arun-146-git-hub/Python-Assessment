""" Classify students by attendance and marks as specified. """

students = {
    "Rahul": {"marks": 85, "attendance": 90},
    "Amit": {"marks": 35, "attendance": 80},
    "Priya": {"marks": 65, "attendance": 70},
    "Neha": {"marks": 45, "attendance": 85},
    "Rohit": {"marks": 90, "attendance": 60}
}

for name, details in students.items():
    marks = details["marks"]
    attendance = details["attendance"]

    if attendance < 75:
        result = "Not Eligible"
    elif marks >= 80:
        result = "Distinction"
    elif marks >= 60:
        result = "First Division"
    elif marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(name, result)
