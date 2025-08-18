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
