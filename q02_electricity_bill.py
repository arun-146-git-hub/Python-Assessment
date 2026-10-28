""" Calculate electricity bill using the stated unit-rate slabs and surcharge. """

units = float(input("Enter electricity units: "))

if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    elif units <= 300:
        bill = units * 10
    else:
        bill = units * 15

    if bill > 3000:
        bill = bill * 1.10

    print("Electricity bill: ₹", round(bill, 2))
