""" Check seat availability and calculate ticket discount by age. """

seats_available = int(input("Enter available seats: "))
if seats_available > 0:
    age = int(input("Enter customer age: "))
    ticket_price = float(input("Enter ticket price: "))

    if age < 5:
        final_price = 0
    elif age <= 12:
        final_price = ticket_price * 0.50
    elif age > 60:
        final_price = ticket_price * 0.70
    else:
        final_price = ticket_price

    print("Ticket price to pay:", final_price)
else:
    print("House Full")
