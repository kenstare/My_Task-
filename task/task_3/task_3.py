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
