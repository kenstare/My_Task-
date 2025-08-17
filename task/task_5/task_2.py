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

