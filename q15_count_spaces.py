""" Count the number of spaces in the given sentence. """

text = "Python is easy to learn"
space_count = 0

for character in text:
    if character == " ":
        space_count += 1

print("Number of spaces:", space_count)
