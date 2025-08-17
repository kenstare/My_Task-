# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.
#   - Convert them to a set to ensure uniqueness.
#   - Create a dictionary where each name is a key and its length is the value.

# - Requirements:
#   - Use `.split(",")` and `set()` to remove duplicates.
#   - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.

names_input = input("Enter three names separated by commas: ")
names_set = set(names_input.split(","))
names_dict = {name: len(name) for name in names_set}
print("\nUnique Names and Their Lengths:")
for name, length in names_dict.items():
    print(f"\t{name}: {length}")
