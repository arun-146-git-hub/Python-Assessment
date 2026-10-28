""" Find numbers divisible by both 3 and 5. """

numbers = [10, 15, 20, 30, 45, 50, 60, 75]
result = [number for number in numbers if number % 3 == 0 and number % 5 == 0]
print(result)
