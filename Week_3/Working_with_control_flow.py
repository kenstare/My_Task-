# Control Flow in Python

# A.Conditional Statements
# 1. if statement
age = 20
if age >= 18:
    print("You are eligible to vote")
# output: You are eligible to vote


# 2. if-else statement
wallet = 400
price = 500

if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")
# output: Insufficient balance.


# 3. if-elif-else
    score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")
# output: Grade: A 


# 4.Nested if statements
    citizen = True

    age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")
# output: You can vote

# B. Loops

# Iterates through each element in a LIST.

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
# output: I like apple
# output: I like banana
# output: I like orange

# Some usecases
# Iterating through shopping lists.
# Checking availability of products.
# Displaying student names, etc.


# Iterates through each element in a TUPLE.This Works like lists, but remember that tuples are immutable.

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")
# output: Point: 0.34654
# output: Point: -0.48585
# output: Point: 0.57477

# Some usecases
# Storing fixed sensor readings.
# Displaying fixed seating positions, etc.


# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
# output: name: Tunde
# output: age: 16
# output: grade: A

# Some usecases
# Reading database records.
# Showing user profile details.
# Checking configuration settings, etc


# Iterates through each element in a STRING. Remember that strings are sequences of characters.

word = "PYTHON"
for char in word:
    print(char)
# output: P
# output: Y
# output: T
# output: H
# output: O
# output: N


## Some usecases
# Counting vowels/consonants.
# Password validation (checking digits/special chars).
# Text analysis, etc.


# 2.While loop

# Using while loop

## Documenting my thoughts##
# Let the loop start with count = 1
# Let it keep printing until count is greater than 5
# Let the loop terminate when the condition is no longer true

## My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1
# output: Number: 1
# output: Number: 2
# output: Number: 3
# output: Number: 4
# output: Number: 5


# Incrementing with `while`

num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
# output: 1 2 3 4 5 6 7 8 9 10


# Decrementing with `while`

timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1
# output: Countdown: 10
# output: Countdown: 9
# output: Countdown: 8
# output: Countdown: 7
# output: Countdown: 6
# output: Countdown: 5
# output: Countdown: 4
# output: Countdown: 3
# output: Countdown: 2
# output: Countdown: 1


# While with User Input
## Keep asking until the user enters a correct password.

password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access Granted!")
# output: Access Granted!


# Keep asking the user for a name until they type "exit".
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")

# ---> I used `break` here. If you dont know what it is or what it is doing, its OK. I will explain it next...
## Useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.


# Loop Control Statements (break, continue and pass)
# 1. Break
for num in range(1, 10):
    if num == 5:
        break
    print(num)

#The loop stops completely when num == 5.
# Stop searching when an item is found.
# Exit when user input matches a condition.
# Prevent unnecessary iterations.

# 2.Continue 
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 3 is skipped, but the loop continues.
## Some usecases
#Skip invalid data.
#Ignore unwanted characters (like spaces in a string).
#Continue running but avoid certain cases, etc.

# 3.Pass
for num in range(1, 6):
    if num == 3:
        pass   # do nothing for now
    else:
        print(num)

# At num == 3, Python executes pass (nothing happens).
## Some usecases
# Writing code structure (to fill in later).
# Placeholders in class/method definitions.
# Temporarily disable parts of code.


# let try while True again 
# Try and think through this...
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
# Menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Choose an option


# Try and use while True for validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")


# LEets make a guess
secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")


# Do you remember this?

balance = 1000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
 



