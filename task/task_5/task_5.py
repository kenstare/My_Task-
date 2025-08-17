#**Task5: Modify Tuple Indirectly**
# Ask a user to enter three items for their shopping list.
# - Store in a tuple shopping_list.
# - Convert it to a list, then ask for two more items to add.
# - Convert back to a tuple and print the updated list using join() to display items separated by " | ".

shopping_list = (
    input("Enter first item for shopping list: "),
    input("Enter second item for shopping list: "),
    input("Enter third item for shopping list: ")
)

shopping_list = list(shopping_list)
shopping_list.append(input("Enter fourth item for shopping list: "))
shopping_list.append(input("Enter fifth item for shopping list: "))
shopping_list = tuple(shopping_list)

print("Updated shopping list:")
print(" | ".join(shopping_list))
