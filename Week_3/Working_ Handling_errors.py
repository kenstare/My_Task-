# Handling Errors in Python

# 1.Syntax Errors
# Common Subtypes of Syntax Errors

# a. IndentationError – Incorrect spacing
from ast import If


for i in range(3):
print(i)   # Wrong indentation

# This will through error except you fix the indentation

Cell In[2], line 2
    print(i)   # Wrong indentation
    ^
# IndentationError: expected an indented block after 'for' statement on line 1

# b. Missing Colon/Parenthesis Error
if 5 > 3   # Missing colon
    print("Hello")

# c. Invalid Syntax – General grammar mistakes.
 print "Hello"   # Missing parentheses in Python 3

# 2. Runtime Errors

# Common Subtypes of Runtime Errors
# a. ZeroDivisionError – Dividing by zero.
x = 10 / 0   # This will throw error

# b. NameError – Using a variable before defining it
print(age)   # age not defined

# c. TypeError – Wrong data type in an operation.
result = "10" + 5   # str + int not allowed

# d. ValueError – Invalid value for a function.
number = int("abc")   # cannot convert string to int

# e. IndexError – Accessing list index out of range.
fruits = ["apple", "banana"]
print(fruits[3])   # Index out of range

# f. KeyError – Accessing a dictionary with a missing key
data = {"name": "Ada"}
print(data["age"])   # Key not found

# g. FileNotFoundError – File does not exist.
f = open("missing.txt")   # File not found


# Handling Runtime Errors
## The `try` Block**

# - It is used to wrap code that might raise an error.

# - If no error occurs Python skips the except block.
try:
    x = 10 / 2
    print("Result:", x)

## The `except` Block**
# - It defines what to do if an error occurs inside try.
# - It can catch specific errors or all errors.

# This is a specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# This is a case of multiple exception

try:
    number = int("abc")   # ValueError
    result = 10 / 0       # ZeroDivisionError

except ValueError:
    print("Invalid conversion to integer.")

except ZeroDivisionError:
    print(" Cannot divide by zero.")


# the `finally` Block**
# - Always runs, whether an error occurred or not.
# - Useful for cleanup tasks (e.g., closing files, releasing resources).

# IF you don't understand this line of code now, It's Ok. But make sure you come back to it once we are done the *File Handling**.

try:
    f = open("sample.txt", "r")
    content = f.read()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Closing file if it was opened.")


# LEts have more example on the application of try-except-finally, but try to read in between the line for better understanding.
balance = 5000  # starting balance

print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)  # convert input to number
    
    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Transaction session closed.")


## **3. Semantic Errors
# common Subtypes of Semantic Errors

# Wrong Condition in Logic

age = 18
if age > 18:   # Should be >=
    print("Eligible to vote")
else:
    print("Not eligible")

# output: Not eligible (wrong result)


# Wrong Formula/Computation
length = 10
width = 5
area = length + width   # should be multiplication
print("Area:", area)

# output: 15 (expected 50)


# Wrong Variable Usage
marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]   #  wrong, should be sum
print("Total:", total)








