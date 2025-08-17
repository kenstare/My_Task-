# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.
  # - Items should come from a list.
  # - Prices are entered by the user.
  # - Display all items and prices, then allow the user to update the price of an item.

# - Requirements:
  # - Use dictionary update method `.update()` or assignment.
  # - Use `.keys()` to display available items.
  # - Use input validation (no advanced functions).

item_prices = {}

# You need to define the items list before using it
items = ['apple', 'banana', 'milk', 'bread']

# Adding items and prices
for item in items:
    while True:
        try:
            price = float(input(f"Enter price for {item}: "))
            item_prices[item] = price
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Displaying all items and prices
print("\nSuper Market Price List:")
for item, price in item_prices.items():
    print(f"\t{item}: #{price:.2f}")

# Updating item prices
while True:
    update_item = input("\nEnter an item to update its price (or 'done' to finish): ")
    if update_item.lower() == 'done':
        break
    if update_item in item_prices:
        while True:
            try:
                new_price = float(input(f"Enter new price for {update_item}: "))
                item_prices[update_item] = new_price
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    else:
        print("Item not found.")

