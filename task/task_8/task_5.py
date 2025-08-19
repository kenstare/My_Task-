# Task5: Store Inventory Update**
# - Create a dictionary called store with items and their available quantities. Example:

store = {"Book": 10, "Pen": 20, "Bag": 5}
# - Ask the user to input the item they want to buy (e.g., "Pen").
# - Ask the user to input the quantity they want to purchase.
# - Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
# - Print the updated dictionary in this format:

# Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
# After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}  


# Task5: Store Inventory Update

# Create a dictionary called store with items and their available quantities
store = {"Book": 500, "Pen": 100, "Bag": 2000}

# Print the inventory before purchase
print(f"Before purchase: {store}")

# Ask the user to input the item they want to buy
item = input("Enter the item you want to buy: ")

# Ask the user to input the quantity they want to purchase
quantity = int(input("Enter the quantity you want to purchase: "))

# Use the assignment operator -= to update the item quantity in the dictionary
store[item] -= quantity

# Print the inventory after purchase
print(f"After purchase: {store}")
