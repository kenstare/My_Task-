print("Welcome to Ofa Telecom Service!")
try:
    ussd = input("Please dial your USSD code (e.g., *123#): ")
    # Semantic error handling: Check for empty USSD input and correct format
    assert ussd, "USSD code cannot be empty."
    assert ussd.startswith("*") and ussd.endswith("#"), "Invalid USSD code format."

    print("\nMenu:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")
    option = input("Choose an option 1, 2, or 3: ")

    # Syntax error handling: Correct Python syntax used throughout

    if option == "1":
        print(f"You selected: Check Balance.\nYour balance is ₦0.01.")
    elif option == "2":
        amount = input("Enter amount to buy airtime: ")
        # Runtime error handling: Check for valid float conversion
        try:
            amount = float(amount)
            assert amount > 0, "Amount must be greater than zero."
            print(f"Your Airtime purchase of ₦{amount:.2f} was successful.")
        except ValueError:
            print("Input Error: Amount must be a number.")
        except AssertionError as ae:
            print(f"Input Error: {ae}")
    elif option == "3":
        amount = input("Enter amount to buy data: ")
        # Runtime error handling: Check for valid float conversion
        try:
            amount = float(amount)
            assert amount > 0, "Amount must be greater than zero."
            print(f"Your Data purchase of ₦{amount:.2f} was successful.")
        except ValueError:
            print("Input Error: Amount must be a number.")
        except AssertionError as ae:
            print(f"Input Error: {ae}")
    else:
        print("Your option selected is invalid.")
except AssertionError as ae:
    print(f"Input Error: {ae}")
except Exception as e:
    print(f"Runtime Error: {e}")

print("Thank you for using Ofa Telecom Service!")