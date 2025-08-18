print("Welcome to Ofa Telecom Service!")
ussd = input("Please dial your USSD code (e.g., *123#): ")
print("\nMenu:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")
option = input("Choose an option 1, 2, or 3: ")
if option == "1":
    print(f"You selected: Check Balance.\nYour balance is ₦0.01.")
elif option == "2":
    amount = float(input("Enter amount to buy airtime: "))
    print(f"Your Airtime purchase of ₦{amount:.2f} was successful.")
elif option == "3":
    amount = float(input("Enter amount to buy data: "))
    print(f"Your Data purchase of ₦{amount:.2f} was successful.")
else:
    print("Your option selected is invalid.")
print("Thank you for using Ofa Telecom Service!")