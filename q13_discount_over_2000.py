""" Apply 20% discount only to prices greater than ₹2,000 and store discounted prices. """

prices = [500, 1200, 2500, 3000, 1500, 5000]
result = [price * 0.80 for price in prices if price > 2000]
print(result)
