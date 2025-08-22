# **Task4: Create a Unique Voters Registration System**
# - Ask for voter names and store in a set.
# - If a voter tries to register twice, display a warning.
# - After registration, display the total number of unique voters.

voters = set()
while True:
    try:
        name = input("Enter voter's name (or 'done' to finish): ")
        # Syntax error handling: correct indentation and syntax used
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")  # Semantic error handling
        if name.strip() == "":
            print("Error: Name cannot be empty.")      # Semantic error handling
            continue
        if name.lower() == 'done':
            break
        if name in voters:
            print("This voter is already registered.")  # Semantic error: duplicate registration
        else:
            voters.add(name)
            print("Voter registered successfully.")
    except Exception as e:  # Runtime error handling
        print(f"Runtime Error: {e}")

print("Total unique voters registered:", len(voters))