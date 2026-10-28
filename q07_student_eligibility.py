""" Check eligibility using attendance and marks. """

students = {
    "Rahul": {"attendance": 85, "marks": 70},
    "Amit": {"attendance": 60, "marks": 80},
    "Priya": {"attendance": 90, "marks": 35},
    "Neha": {"attendance": 78, "marks": 55}
}

for name, details in students.items():
    attendance = details["attendance"]
    marks = details["marks"]

    if attendance >= 75:
        if marks >= 40:
            status = "Eligible"
        else:
            status = "Failed in Exam"
    else:
        status = "Not Eligible"

    print(name, status)
