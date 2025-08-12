# single quotes
name = 'Ada'
print(name)


# double quotes
greeting = "Hello"
print(greeting)


# triple quotes (for multi-line string)
story = '''Once upon a time,
there was a codes called ada.'''
print(story)


# string with numbers and symbols 
password = "P@ssw0rd!"
print(password)


# string operations 
# indexing

word = "python"
print(word[0])   # p
print(word[-1])  # n

# slicing
word = "python"
print(word[1:4])  # pyph
print(word[2:])   # thon
print(word[:3])   # pyt
print(word[::2])  # pto
print(word[::-1])

# String concatenation and repetition
# concatenation
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World


# repetition
a = "Hi!"
print(word * 3) # Hi! Hi! Hi!


# string searchin & checking
# membership
text = "python programming"
print("python" in text)    # True
print("java" not in text)  # True


# find () / refind ()
text = "Hello World"
print(text.find("0"))  # 4
print(text.refind("o"))  # 7


#  index() / rindex()
text = "Hello World"
print(text.index("o"))  # 6


# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))    # True











