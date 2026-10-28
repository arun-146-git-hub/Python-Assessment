""" Separate positive deposits and negative withdrawals. """

transactions = [5000, -2000, 3000, -1000, 7000, -500]
deposits = [amount for amount in transactions if amount > 0]
withdrawals = [amount for amount in transactions if amount < 0]

print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
