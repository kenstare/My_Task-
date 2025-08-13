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

 
# Task_2
# Write a program to count the number of characters in a string without using len()
character = "python"
count = 0
for char in character:
#     count += 1
    print(character, "has", count, "characters.")


# Write a program to reverse a string without using slicing ([::-1]).
def reverse_string(s):
    reversed_str = ""
    for chara in s:
        reversed_str = chara + reversed_str
    return reversed_str

print(reverse_string("python"))

#  Given a string with extra spaces, remove the leading and trailing spaces.
def remove_extra_spaces(s):
    start = 0
    end = len(s) - 1
    while start <= end and s[start] == " ":
        start += 1
    while end >= start and s[end] == " ":
        end -= 1
    return s[start:end + 1]
print(remove_extra_spaces("   python   "))

# Ask the user to enter a sentence and print the number of vowels in it.
def count_vowels(s):
    vowels = "joy"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


#  Convert a string "1234" to an integer and multiply it by 2
def convert_and_multiply(s):
    num = int(s)
    return num * 2

# Task 3

# Given "apple,banana,orange", split the string into a list of fruits
def split_fruits(s):
    return s.split(",")


# Ask the user for a sentence and print each word on a new line.
def print_words(sentence):
    words = sentence.split("Ola")
    for word in words:
        print(word)
    

# Replace all spaces in a string with underscores (_)
def replace_spaces_with_underscores(s):
    return s.replace(" ", "_")


# Count how many times the letter "a" appears in "Banana"
def count_letter_a(s):
    count = 0
    for char in s:
        if char == "a":
            count += 1
    return count


# Check if a given string starts with "https://"
def starts_with_https(s):
    return s.startswith("https://")
