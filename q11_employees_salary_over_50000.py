""" Find employees earning more than ₹50,000. """

employees = [
    {"name": "Amit", "salary": 45000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Neha", "salary": 75000},
    {"name": "Rohit", "salary": 35000}
]
result = [employee["name"] for employee in employees if employee["salary"] > 50000]
print(result)
