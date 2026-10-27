""" Find the sum of even numbers from 1 to 100. """

total = 0
for number in range(2, 101, 2):
    total += number
print("Sum of even numbers:", total)
