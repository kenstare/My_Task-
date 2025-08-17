#**Task 3: Word Counter**
#- Ask the user for a sentence.
#- Split the sentence into a list of words.
#- Print how many words are in the sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"There are {len(words)} words in the sentence.")
