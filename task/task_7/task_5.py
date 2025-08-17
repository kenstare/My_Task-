# **Task5: Contact Quick Lookup**
# - Store three names and their phone numbers in two separate tuples.
#   - Create a dictionary from them using `dict(zip(...))`.
#   - Ask the user for a name and display the corresponding number (or an error message).
# - Requirements:
#   - Use `zip()` and `dict()` to combine tuples.
#   - Use `.get()` for safe retrieval.
#   - No loops.

names = ("Ayo", "Femi", "Kemi")
phone_numbers = ("08154693540", "09165560361", "07063519730")

contact_dict = dict(zip(names, phone_numbers))

user_input = input("\nEnter a name to look up their phone number: ")
phone_number = contact_dict.get(user_input, "Not found.")
print(f"Phone number for {user_input}: {phone_number}")
