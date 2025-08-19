# Task3: Online Store Cart Calculation**
# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
# - Start with an empty cart total (cart_total = 0).
# - Use assignment operators (+=) to add the price of some items into cart_total.
# - Print the list of items and the total price using an f-string like this:

# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600 

# Task3: Online Store Cart Calculation

# List of items available in the store
items = ["Book", "Pen", "Bag", "Yam"]

# Corresponding prices for each item
prices = [2500, 500, 2000, 1500]

# Start with an empty cart total
cart_total = 0

# Add the price of selected items to cart_total using assignment operator
cart_total += prices[0]  # Book
cart_total += prices[1]  # Pen
cart_total += prices[2]  # Bag
cart_total += prices[3]  # Yam

# Print the list of items and the total price
print(f"Items: {items}")
print(f"Total Price: ₦{cart_total}")
