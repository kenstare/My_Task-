# **Task4: Create a Unique Voters Registration System**
# - Ask for voter names and store in a set.
# - If a voter tries to register twice, display a warning.
# - After registration, display the total number of unique voters.

voters = set()
while True:
    name = input("Enter voter's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    if name in voters:
        print("This voter is already registered.")
    else:
        voters.add(name)
        print("Voter registered successfully.")

print("Total unique voters registered:", len(voters))