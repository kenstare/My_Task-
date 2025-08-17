# **Task 6: Word Analyzer**
# - Ask the user to input a word.
# - Print the length of the word.
# - Check if it is all uppercase, all lowercase, or title case.
# - Reverse the word using slicing. 

word = input("Enter a word: ")
print(f"The length of the word is: {len(word)}")
if word.isupper():
    print("The word is all uppercase.")
elif word.islower():
    print("The word is all lowercase.")
elif word.istitle():
    print("The word is in title case.")
else:
    print("The word is in mixed case.")
print(f"The reversed word is: {word[::-1]}")
