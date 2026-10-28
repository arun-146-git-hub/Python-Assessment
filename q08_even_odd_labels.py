""" Replace each number with Even or Odd. """

numbers = [10, 15, 20, 25, 30]
result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(result)
