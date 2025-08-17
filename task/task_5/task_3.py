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
