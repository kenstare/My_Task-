customer_name = input("Enter customer's full name: ")
kwh_units = int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit: "))
total = kwh_units * cost_per_unit
print(f"\nElectricity Bill Receipt\nName: {customer_name}\nUnits Consumed: {kwh_units}\nCost per Unit: ₦{cost_per_unit:.2f}\nTotal Bill: ₦{total:,.2f}")
