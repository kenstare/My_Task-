# **Task1: Fruit collector**
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

favourite_fruits = set()
for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    favourite_fruits.add(fruit)

print("Your favourite fruits are:")
print(favourite_fruits)