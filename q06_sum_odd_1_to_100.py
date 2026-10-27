""" Find the sum of odd numbers from 1 to 100. """

total = 0
for number in range(1, 101, 2):
    total += number
print("Sum of odd numbers:", total)
