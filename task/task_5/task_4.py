
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