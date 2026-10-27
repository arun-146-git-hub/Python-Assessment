""" Calculate result for three subjects using the specified thresholds. """

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    percentage = (mark1 + mark2 + mark3) / 3
    print("Percentage:", percentage)

    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    else:
        print("Pass")
else:
    print("Fail")
