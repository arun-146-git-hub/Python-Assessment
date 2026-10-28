""" Classify dictionary values as Large Even, Even or Odd. """

data = {"a": 10, "b": 15, "c": 25, "d": 30, "e": 40}

for key, value in data.items():
    if value % 2 == 0:
        if value > 20:
            category = "Large Even"
        else:
            category = "Even"
    else:
        category = "Odd"
    print(key, category)
