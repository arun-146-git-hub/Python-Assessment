""" Classify products by price. """

products = {"Mobile": 15000, "Mouse": 500, "Laptop": 60000, "Keyboard": 1200}

for product, price in products.items():
    if price >= 5000:
        category = "Premium Product"
    elif price >= 1000:
        category = "Expensive Product"
    else:
        category = "Affordable Product"
    print(product, category)
