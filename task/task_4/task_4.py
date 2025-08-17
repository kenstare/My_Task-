# **Task 4: Name Organizer**
#- Ask the user to enter 5 names (separated by spaces).

#- Convert all names to lowercase.
#- Sort the list alphabetically.
# - Display them one name per line.
# -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

names = input("Enter 5 names (separated by spaces): ").split()
names = [name.lower() for name in names]
names.sort()
print("Here are the names in alphabetical order:")
for name in names:
    print(name)