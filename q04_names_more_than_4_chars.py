""" Find names with more than four characters. """

names = ["Amit", "Rahul", "Neha", "Rohit", "Sneha"]
result = [name for name in names if len(name) > 4]
print(result)
