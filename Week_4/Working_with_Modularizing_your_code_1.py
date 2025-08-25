# Modularizing your code 1

# Common Categories of Built-in Functions**

# 1. Input and Output Functions

print() # Displays output.

input() # Takes user input.

# 2. Type Conversion Functions

# `int()`, `float()`, `str()`, `bool()`, `list()`, `dict()`, `tuple()`, `set()`

# 3. Mathematical Functions

# bs() # Absolute value

# pow(x, y) # x raised to power y

# ound() # Round numbers to the defined decimal places

# min(), max() # Find smallest/largest

# 4. Sequence and Collection Functions

# len() # Length of a sequence

# sum() # Sum of elements

# sorted() # Sort items

# enumerate() # Track index and value

# 5. Utility Functions

# type() # Shows the type of an object(variables,datatypes, data structures, functions, classes)

# id() # Returns unique ID of object in memory

# help() # Documentation about an object


# 6. Special Built-ins


# range() # Generates a sequence of numbers

# zip() # Combines two lists element by element

# map() # Applies a function to all elements in a sequence

# filter() # Filters elements in a sequence based on condition


# see Examples of use here 

# range()
for i in range(3):
    print(i)      # output 0, 1, 2

    #zip()
    names = ["Esther", "Precious", "kenny"]
    scores = [85, 90, 75]
    for n, s in zip(names, scores):
        print(n, "scored",s)

# it's ok, if don't what lambdas is  or how to use it. I will touch on it later. just focus on the outputs
# map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # output [1, 4, 9, 16]

# filter()
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # output [2, 4]


# Student performance & Feedback System

# Step 1: Input student data
name1 = input("Enter First student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter Second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter Third student name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n,s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

    # Step 4: Summary using built-ins
    total = sum(scores)
    average = round(total / len(scores), 2)
    highest = max(scores)
    lowest = min(scores)

    print("\nPerformance Summary:")
    print("Total Score:", total)
    print("Average Score:", average)
    print("Highest Score:", highest)
    print("Lowest Score:", lowest)

    # Step 5: Ranking (using sorted and zip)
    ranked = sorted(zip(scores, names), reverse=True)
    print("\nRanking:")
    for rank, (score, name) in enumerate(ranked, 1):
        print(f"{rank}. {name} - {score}")

# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list:", id(scores))

# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)

# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names) 

# Step 9: Use help() to show documentation of len
print("\nHelp on len():")
help(len)



# User Defined Functions   


# Defining a function
def greet():
    print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()


# Function Arguments And Parameters

# Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to Python learning!")

# Calling with parameter- the actual name
greet("Class rep")
greet("Ridwan")



# When to Use return, print(), and yield keywords inside a function 
# A. Print()
def greet(name):
    print("Hello", name)


# Function call
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)


# B. return 
def add(a, b):
    return a + b

# Function call

result = add(4, 6)
print("The sum is:", result)

# Note the output and compare it with that of print()


# C. yieid 
def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.




# 1. Positional Arguments**
# - These are the most common.

# - The order matters: values are assigned to parameters in the same order as they appear.

# - Think of it like lining up children in the same order as roll call.

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
introduce("Ngozi", "AI Engineering")   # Correct order

# Change the arrangment and watch the output

introduce("AI Engineering","Ngozi")   # Incorrect order, this will throw a semantic error



# 2. Keyword Arguments

# - Here, you explicitly mention the parameter name when calling the function.

#  Order doesn’t matter, since Python knows which value goes where.

# - Think of it like addressing an envelope by name instead of position in line.

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the output

introduce(track = "AI Engineering",name = "Ngozi")   # Here you notice that order does not matter


# 3. Default Arguments
# - HERE, you can give parameters a default value.

# - Even if no value is provided when calling, the default is used.

# - Think of it like a restaurant menu where rice is served by default if you don’t choose otherwise.

def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track)

# function call
# Without specifying the default argument, but watch the ouput
introduce("Paul")  


# Specify the default argument and watch the output

introduce("Tunji Paul", track = "AI Development")


# 4. Varying Length Arguments

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call 
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# b. keyword argument (dictionary)**

# - Collects extra keyword arguments into a dictionary.

# - Think of it like a labeled container where each item has a name tag.

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest="Block Chain")


# Lets implement on full code

# Define student profile function

# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together

def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile  # Do you remember `return` and why it is used? We are using it so it can be reused in other places



# ---------- LEts test ----------

# Example 1: Using only positional arguments
print(participant_profile("Peter", 24))

# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))

# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))


# Namespaces and Scope

# Global Namespace
employee = "General Employee"  

def IT_department():
    # Local Namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)

def Training_department():
    # Local Namespace inside Training_department
    employee = "Chris (Training)"
    print("Inside Training Department:", employee)

print("In Global Namespace:", employee)  # Refers to global variable

IT_department()   # Uses local variable in IT
Training_department()   # Uses local variable in Training

# Using a built-in namespace function
print("Length of 'Python':", len("Python"))  

# So 'Chris' can exist in more than one namespace without conflict.
# Please, take your time to study the output carefully.


# cope

# - Scope defines where in the code a name is accessible.
# Python follows the *LEGB Rule* (order of search for a variable):

# L – Local → Inside the current function.

# E – Enclosing → Inside any enclosing function(s).

# G – Global → At the top level of the script/module.

# B – Built-in → Python’s built-in functions/objects.

x = "global x"   # Global Namespace

def outer():
    x = "enclosing x"  # Enclosing Namespace
    
    def inner():
        x = "local x"  # Local Namespace
        print("Inside inner:", x)  # Local wins
    
    inner()
    print("Inside outer:", x)  # Enclosing
    
outer()
print("In global:", x)  # Global

# Watch the output
# Notice how Python searches in the order Local → Enclosing → Global → Built-in (LEGB).


### Global keyword

# Used when you want to modify a global variable inside a function.

x = 5

def change_global():
    global x
    x = 10   # modifies the global x

change_global()
print(x)  # Output: 10

# Watch the output




# nonlocal keyword

#Used in nested functions when you want to modify the variable from the enclosing scope (not global).

def outer():
    x = "outer x"
    
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)
    
    inner()
    print("Inside outer:", x)

outer()

# Watch the output



# Lambda Function

# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))         
print(square_lambda(5))  

# Watch the output and note the difference


# This one has more that one arguments.

add = lambda a, b: a + b
print(add(3, 7))  # Output: 10


# Let us lambda to apply the square function to a list

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]


# Lets use lambda to filter even numbers 

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [10, 20, 30]


# Lets use lambda to sort the tuple within a list.

students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

  
# Output: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)

# Output: [('Chika', 22), ('Ayo', 20), ('Bola', 18)]

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)

# Output: [('Ayo', 20), ('Bola', 18), ('Chika', 22)]
