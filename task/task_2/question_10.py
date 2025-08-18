school = input("Enter school name: ")
tuition_fee = float(input("Enter tuition fee: "))
hostel_fee = float(input("Enter hostel fee: "))
feeding_fee = float(input("Enter feeding fee: "))
total = tuition_fee + hostel_fee + feeding_fee
print(f"\nSchool: {school}\nTuition Fee: ₦{tuition_fee:,.2f}\nHostel Fee: ₦{hostel_fee:,.2f}\nFeeding Fee: ₦{feeding_fee:,.2f}\nTotal: ₦{total:,.2f}")
