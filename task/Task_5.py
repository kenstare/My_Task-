# **Task1:  Create and Display**
# - Ask the user to enter three favorite Nigerian dishes (one at a time).
# - Store them in a tuple called dishes.
# - Print the tuple in a single line, separating items with commas.
# - Use the \n escape sequence to print each dish on a new line.

dishes = (
    input("Enter first dish: "),
    input("Enter second dish: "),
    input("Enter third dish: ")
)

print(dishes)
print("\n".join(dishes))


# **Task2: Tuple and Input**
# - Ask the user for 5 best friends’ names.
# - Store them in a tuple friends.
# - Print the tuple in reverse order.

friends = (
    input("Enter first friend's name: "),
    input("Enter second friend's name: "),
    input("Enter third friend's name: "),
    input("Enter fourth friend's name: "),
    input("Enter fifth friend's name: ")
)

print(friends[::-1])


# **Task3: Tuple Operations**
# - Create a tuple of 5 Nigerian states entered by the user.
  # - Print the first state and last state.
  # - Check if "Lagos" is in the tuple and print "Yes" or "No".
  # - Print the number of states entered.
    # - (Hint: use the tuple membership)
    
states = (
        input("Enter first state: "),
        input("Enter second state: "),
        input("Enter third state: "),
        input("Enter fourth state: "),
        input("Enter fifth state: ")
    )
print("First state:", states[0])
print("Last state:", states[-1])
print("Is Lagos in the states?", "Yes" if "Lagos" in states else "No")
print("Number of states entered:", len(states))


# **Task4: Tuple Unpacking**
 # - Ask a user for their;
  # - First name
  # - Age
  # - Favorite color
  # - Home town
  # - Store them in a tuple profile and unpack into variables.
  # - Print and use  escape sequence to align each piece of information nicely.

profile = (
      input("Enter your first name: "),
      input("Enter your age: "),
      input("Enter your favorite color: "),
      input("Enter your home town: ")
  )

first_name, age, favorite_color, home_town = profile

print(f"First Name:\t{first_name}")
print(f"Age:\t\t{age}")
print(f"Favorite Color:\t{favorite_color}")
print(f"Home Town:\t{home_town}")


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


# **Task6: Attendance Tracker**
# - Write a Python program that;
# - Stores the days of the week in a tuple.
# - Stores the months of the year in another tuple.
# - Asks the user to enter:
#   - Student’s name
#   - Gender
#   - Course Track
#   - Current month number (1-12)
#   - Current day number (1-7)

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

student_name = input("Enter student's name: ")
gender = input("Enter gender: ")
course_track = input("Enter course track: ")
current_month = int(input("Enter current month number (1-12): "))
current_day = int(input("Enter current day number (1-7): "))
