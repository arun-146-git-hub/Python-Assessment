""" Extract digits from a string into a list. """

data = "Python123Programming456"
result = [character for character in data if character.isdigit()]
print(result)
