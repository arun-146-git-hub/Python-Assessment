""" Give a 10% discount to prices of ₹1,000 or more, otherwise 5%. """

prices = [500, 1200, 800, 2000, 1500]
result = [price * 0.90 if price >= 1000 else price * 0.95 for price in prices]
print(result)
