#**Task 2: Shopping List Manager**
#- Create an empty list.
#- Ask the user to enter 3 shopping items (one by one).
#- Add them to the list.
#- Display the list as a single string, separated by commas.

shopping_list = []
for i in range(3):
    item = input(f"Enter shopping item {i+1}: ")
    shopping_list.append(item)

print("Your shopping list is:")
print(", ".join(shopping_list))