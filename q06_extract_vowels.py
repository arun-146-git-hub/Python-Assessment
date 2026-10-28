""" Extract vowels from a string into a list. """

text = "programming"
result = [character for character in text if character in "aeiouAEIOU"]
print(result)
