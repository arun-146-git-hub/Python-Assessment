""" Find the largest number in a list using a for loop. """

data = [22, 55, 12, 89, 34, 67]
largest = data[0]

for number in data:
    if number > largest:
        largest = number

print("Largest number:", largest)
