""" ATM withdrawal using nested conditions. """

correct_pin = "1234"
pin = input("Enter PIN: ")
balance = 10000

if pin == correct_pin:
    amount = int(input("Enter withdrawal amount: "))
    if amount % 100 == 0:
        if balance >= amount:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be a multiple of 100.")
else:
    print("Invalid PIN")
