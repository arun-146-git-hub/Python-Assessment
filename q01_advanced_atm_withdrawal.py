""" Advanced ATM challenge: PIN, active account, amount checks, minimum balance and extra verification. """

correct_pin = "1234"
pin = input("Enter PIN: ")
account_active = input("Is the account active? (yes/no): ").strip().lower() == "yes"
balance = float(input("Enter account balance: "))

if pin != correct_pin:
    print("Invalid PIN")
elif not account_active:
    print("Account is not active")
else:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Amount must be positive")
    elif amount % 100 != 0:
        print("Amount must be a multiple of ₹100")
    elif amount > balance:
        print("Insufficient balance")
    elif balance - amount < 500:
        print("Minimum balance of ₹500 must remain")
    else:
        if amount > 20000:
            verification = input("Extra verification passed? (yes/no): ").strip().lower()
            if verification != "yes":
                print("Extra verification failed")
                raise SystemExit
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
