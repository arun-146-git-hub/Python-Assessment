""" Find the smallest number in a list. """

data = [22, 55, 12, 89, 34, 67]
smallest = data[0]

for number in data:
    if number < smallest:
        smallest = number

print("Smallest number:", smallest)
