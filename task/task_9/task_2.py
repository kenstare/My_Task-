# Task5: Store Inventory Update

# Create a dictionary called store with items and their available quantities
store = {"Book": 10, "Pen": 20, "Bag": 5}

# Print the inventory before purchase
print(f"Before purchase: {store}")

# Ask the user to input the item they want to buy
item = input("Enter the item you want to buy: ")

# Ask the user to input the quantity they want to purchase
quantity = int(input("Enter the quantity you want to purchase: "))

# Use the assignment operator -= to update the item quantity in the dictionary
if item in store and store[item] >= quantity:
    store[item] -= quantity
else:
    print("Sorry, item not available or insufficient quantity.")

# Print the inventory after purchase
print(f"After purchase: {store}")