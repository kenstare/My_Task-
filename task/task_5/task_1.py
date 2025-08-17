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