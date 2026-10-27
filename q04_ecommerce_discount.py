""" Calculate discount based on cart amount and premium membership. """

cart_amount = float(input("Enter cart amount: "))
premium_member = input("Premium member? (yes/no): ").strip().lower()

if cart_amount >= 5000:
    if premium_member == "yes":
        discount_rate = 0.20
    else:
        discount_rate = 0.10
else:
    if premium_member == "yes":
        discount_rate = 0.05
    else:
        discount_rate = 0

discount = cart_amount * discount_rate
final_amount = cart_amount - discount

print("Discount:", discount)
print("Final amount:", final_amount)
