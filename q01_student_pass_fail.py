""" Print Pass or Fail for each student in a dictionary. """

students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55
}

for name, marks in students.items():
    if marks >= 40:
        print(name, "Pass")
    else:
        print(name, "Fail")
