""" Replace negative numbers with zero. """

numbers = [10, -5, 20, -8, 30, -2]
result = [number if number >= 0 else 0 for number in numbers]
print(result)
