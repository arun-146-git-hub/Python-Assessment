""" Take a number from the user and print its multiplication table. """

number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")
