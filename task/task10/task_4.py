
# **Task 6: Word Analyzer**
# - Ask the user to input a word.
# - Print the length of the word.
# - Check if it is all uppercase, all lowercase, or title case.
# - Reverse the word using slicing.
# - Handle syntax, runtime, and semantic errors.

try:
    word = input("Enter a word: ")

    # Semantic error handling: Check for empty input
    if not word or not word.isalpha():
        raise ValueError("Input must be a non-empty word containing only letters.")

    print(f"The length of the word is: {len(word)}")

    # Syntax error handling: Correct Python syntax used throughout

    # Case checks
    print(
        "The word is all uppercase." * word.isupper() +
        "The word is all lowercase." * word.islower() +
        "The word is in title case." * word.istitle() +
        "The word is in mixed case." * (not (word.isupper() or word.islower() or word.istitle()))
    )

    print(f"The reversed word is: {word[::-1]}")

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Runtime Error: {e}")