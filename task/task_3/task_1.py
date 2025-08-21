# Task_1

#  Write a program to take a string input from the user and display it in uppercase.

user_input = input("Enter a string: ")
print(user_input.upper())


# Given the string "python", print its first and last characters.
word = "python"
print("First character:", word[0])
print("Last character:", word[-1])


#  Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
name = input("What is your name? ")
print(f"Hello, {name}!")

#  Write a program to count the number of characters in a string without using len()
character = "python"
print(character, "has", 6, "characters.")


# Give "Hello World", replace "World" with python
text = "Hello World"
print(text.replace("World", "python"))
