""" Find names of students scoring 60 or more. """

students = [
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 45},
    {"name": "Neha", "marks": 90},
    {"name": "Rohit", "marks": 55}
]
result = [student["name"] for student in students if student["marks"] >= 60]
print(result)
