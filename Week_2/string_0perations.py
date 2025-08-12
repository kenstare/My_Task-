# upper case()
name = "Ada Balogun"
print(name.upper())  # ADA BALOGUN
print(name.lower())  # ada balogun
print(name.title())  # Ada Balogun
print(name.capitalize())  # Ada balogun


# lower case()
sentence = "python is amazing"
print(sentence.lower())  # python is amazing
print(sentence.upper())  # PYTHON IS AMAZING
print(sentence.title())  # Python Is Amazing
print(sentence.capitalize())  # Python is amazing


# strip
text = str(input("Abuja"))
print(text.strip())  # "Abuja"


# replace
message = "I love kenny"
print(message.replace("kenny", "john"))  # I love john


# swapcase()
text = "Hello ABEOKUTA"
print(text.swapcase())  # HELLO abeokuta


# lstrip()
text = "   Nigeria"
print(text.lstrip())  # "Nigeria"


# rstrip()
text = "Nigeria   "
print(text.rstrip())  # "Nigeria"


# split()
fruits = "mango orange banana"
print(fruits.split())  # ['mango', 'orange', 'banana']


# rsplit()
text = "one,two,three,four"
print(text.rsplit(",",2)) # ['three', 'four', 'one,two']


# splitlines()
text = "Line 1\nLine 2\nLine 3"
print(text.splitlines())  # ['Line 1', 'Line 2', 'Line 3']


# join()
words = ["I", "love", "python"]
print(" ".join(words))  # I love python


# center()
text = "python"
print(text.center(20, "-"))  # "-------python--------"


# ljust()
text = "   python   "
print(text.ljust(10, "*"))  # "python****"


# rjust()
text = "python"
print(text.rjust(10, "*"))  # "****python"


# zfill()
text = "42"
print(text.zfill(5))  # "00042"


# isalpha()
print("Lagos".isalpha())  # True
print("Lagos123".isalpha())  # False


# isdigit()
print("12345".isdigit())  # True
print("12345a".isdigit())  # False


# isalnum()
print("python3".isalnum())  # True
print("python 3".isalnum())  # False


# isspace()
print("   ".isspace())  # True
print("   a".isspace())  # False


# islower()
print("hello".islower())  # True
print("Hello".islower())  # False


# isupper()
print("HELLO".isupper())  # True
print("Hello".isupper())  # False


# istitle()
print("Hello World".istitle())  # True
print("Hello world".istitle())  # False


# Reversed
text = "Hello"
print(text[::-1])  # olleH
