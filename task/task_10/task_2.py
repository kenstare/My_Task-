# Task5: Store Inventory Update

# Create a dictionary called store with items and their available quantities
store = {"Book": 10, "Pen": 20, "Bag": 5}

# Print the inventory before purchase
print(f"Before purchase: {store}")

try:
    # Ask the user to input the item they want to buy
    item = input("Enter the item you want to buy: ")

    # Semantic error handling: Check if item exists in store
    if item not in store:
        raise ValueError("Item not found in store.")

    # Ask the user to input the quantity they want to purchase
    quantity = int(input("Enter the quantity you want to purchase: "))

    # Runtime error handling: Check for valid quantity
    if quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    # Use the assignment operator -= to update the item quantity in the dictionary
    if store[item] >= quantity:
        store[item] -= quantity
    else:
        print("Sorry, insufficient quantity.")

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Runtime Error: {e}")

# Print the inventory after purchase
print(f"After purchase: {store}")