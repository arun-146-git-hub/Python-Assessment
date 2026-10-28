""" Check age, learner license and driving test score. """

age = int(input("Enter age: "))

if age >= 18:
    learner_license = input("Do you have a learner license? (yes/no): ").strip().lower()
    if learner_license == "yes":
        score = float(input("Enter driving test score: "))
        if score >= 60:
            print("Eligible for driving license")
        else:
            print("Driving test not passed")
    else:
        print("Learner license required")
else:
    print("Age requirement not met")
