account = {
    "name": "Pavan",
    "card_valid": True,
    "pin": "1234",
    "balance": 5000.0,
    "transactions": []
}

while True:
    card = input("Insert card? (yes/no): ").lower()

    if card == "yes":
        print("\nReading card...")

        if account["card_valid"]:
            print("Card Verified Successfully.")
            print(f"Welcome, {account['name']}!")
            break
        else:
            print("Invalid Card.")
            exit()

    elif card == "no":
        print("No card inserted.")
        print("Thank you for visiting.")
        exit()

    else:
        print("Invalid input. Please enter yes or no.")

attempts = 3

while attempts > 0:
    entered_pin = input("\nEnter your 4-digit PIN: ")

    if not entered_pin.isdigit():
        print("PIN should contain only numbers.")
        continue

    if len(entered_pin) != 4:
        print("PIN must be exactly 4 digits.")
        continue

    if entered_pin == account["pin"]:
        print("\nLogin Successful.")
        break

    attempts -= 1

    if attempts > 0:
        print("Incorrect PIN.")
        print("Attempts Left:", attempts)

    else:
        print("\n==========================================")
        print("ACCOUNT LOCKED")
        print("You have entered the wrong PIN")
        print("three consecutive times.")
        print("Your account has been locked")
        print("for the next 24 hours.")
        print("Please try again after 24 hours.")
        print("==========================================")
        exit()

while True:
    print("\n========== XYZ BANK ATM ==========")
    print("1. Cash Withdrawal")
    print("2. Cash Deposit")
    print("3. Balance Enquiry")
    print("4. Mini Statement")
    print("5. PIN Change")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    if choice == 1:
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Invalid amount.")

        elif amount % 100 != 0:
            print("Withdrawal amount must be in multiples of 100.")

        elif amount > account["balance"]:
            print("Insufficient Balance.")

        else:
            account["balance"] -= amount
            account["transactions"].append(f"Withdrawn ${amount:.2f}")
            print("Please collect your cash.")
            print(f"Remaining Balance: ${account['balance']:.2f}")

    elif choice == 2:
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Invalid amount.")

        else:
            account["balance"] += amount
            account["transactions"].append(f"Deposited ${amount:.2f}")
            print("Amount Deposited Successfully.")
            print(f"Current Balance: ${account['balance']:.2f}")

    elif choice == 3:
        print(f"\nCurrent Balance: ${account['balance']:.2f}")

    elif choice == 4:
        print("\n========== MINI STATEMENT ==========")

        if len(account["transactions"]) == 0:
            print("No transactions available.")
        else:
            for transaction in account["transactions"][-5:]:
                print(transaction)

    elif choice == 5:
        current_pin = input("Enter Current PIN: ")

        if current_pin != account["pin"]:
            print("Incorrect Current PIN.")
            continue

        new_pin = input("Enter New PIN: ")

        if not new_pin.isdigit():
            print("PIN should contain only numbers.")
            continue

        if len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            continue

        confirm_pin = input("Confirm New PIN: ")

        if new_pin != confirm_pin:
            print("PINs do not match.")
            continue

        account["pin"] = new_pin
        account["transactions"].append("PIN Changed")
        print("PIN Changed Successfully.")

    elif choice == 6:
        print("\nPlease collect your card.")
        print("Thank you for using XYZ Bank ATM.")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")