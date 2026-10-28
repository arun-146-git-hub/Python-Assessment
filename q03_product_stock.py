""" Display stock status for each product. """

products = {"Laptop": 10, "Mouse": 3, "Keyboard": 0, "Monitor": 7, "Printer": 2}

for product, stock in products.items():
    if stock == 0:
        status = "Out of Stock"
    elif stock <= 5:
        status = "Low Stock"
    else:
        status = "Available"
    print(product, status)
