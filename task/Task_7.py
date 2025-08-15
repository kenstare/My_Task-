# **Task1: Student Bio Data Storage**

# - Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
  # - Courses should be stored as a list.
  # - Display the bio-data neatly using escape sequences.
  # - Requirements:
  # - Use `input()` to collect details.
  # - Use dictionary operations `(dict[key] = value)` to store data.
  # - Use `print()` formatting with `\n` and `\t` for better output.

def collect_student_bio_data():
    student_data = {}

    # Collecting basic information
    student_data['name'] = input("Enter student's name: ")
    student_data['age'] = int(input("Enter student's age: "))
    student_data['gender'] = input("Enter student's gender: ")

    # Collecting courses
    courses = []
    while True:
        course = input("Enter a course (or 'done' to finish): ")
        if course.lower() == 'done':
            break
        courses.append(course)
    student_data['courses'] = courses

    return student_data

def display_student_bio_data(student_data):
    print("\nStudent Bio Data:")
    for key, value in student_data.items():
        if isinstance(value, list):
            value = ", ".join(value)
        print(f"\t{key}: {value}")

# Main program
student_bio = collect_student_bio_data()
display_student_bio_data(student_bio)


# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.
  # - Items should come from a list.
  # - Prices are entered by the user.
  # - Display all items and prices, then allow the user to update the price of an item.

# - Requirements:
  # - Use dictionary update method `.update()` or assignment.
  # - Use `.keys()` to display available items.
  # - Use input validation (no advanced functions).

item_prices = {}

# You need to define the items list before using it
items = ['apple', 'banana', 'milk', 'bread']

# Adding items and prices
for item in items:
    while True:
        try:
            price = float(input(f"Enter price for {item}: "))
            item_prices[item] = price
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Displaying all items and prices
print("\nSuper Market Price List:")
for item, price in item_prices.items():
    print(f"\t{item}: #{price:.2f}")

# Updating item prices
while True:
    update_item = input("\nEnter an item to update its price (or 'done' to finish): ")
    if update_item.lower() == 'done':
        break
    if update_item in item_prices:
        while True:
            try:
                new_price = float(input(f"Enter new price for {update_item}: "))
                item_prices[update_item] = new_price
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    else:
        print("Item not found.")



# **Task3: Days and Activities Pairing**
# - Store days of the week in a tuple and ask the user to input an activity for three specific days.
  # - Use dictionary comprehension to pair days and activities.
  # - Print the dictionary.

# - Requirements:
  # - Use a tuple for days.
  # - Use {day: activity for day, activity in `zip(..., ...)`}.
  # Tip: Research on how to use `zip()`  

days = ("Monday", "Tuesday", "Wednesday")
activities = []

for day in days:
    activity = input(f"Enter an activity for {day}: ")
    activities.append(activity)

# Pairing days and activities using dictionary comprehension
day_activity_dict = {day: activity for day, activity in zip(days, activities)}

# Printing the dictionary
print("\nDays and Activities:")
for day, activity in day_activity_dict.items():
    print(f"\t{day}: {activity}")


# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.
#   - Convert them to a set to ensure uniqueness.
#   - Create a dictionary where each name is a key and its length is the value.

# - Requirements:
#   - Use `.split(",")` and `set()` to remove duplicates.
#   - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.

names_input = input("Enter three names separated by commas: ")
names_set = set(names_input.split(","))
names_dict = {name: len(name) for name in names_set}
print("\nUnique Names and Their Lengths:")
for name, length in names_dict.items():
    print(f"\t{name}: {length}")



# **Task5: Contact Quick Lookup**
 # - Store three names and their phone numbers in two separate tuples.
 #   - Create a dictionary from them using `dict(zip(...))`.
 #   - Ask the user for a name and display the corresponding number (or an error message).
# - Requirements:
  # - Use `zip()` and `dict()` to combine tuples.
  # - Use `.get()` for safe retrieval.
  # - No loops.

names = ("Ayo", "Femi", "Kemi")
phone_numbers = ("08154693540", "09165560361", "07063519730")

contact_dict = dict(zip(names, phone_numbers))

user_input = input("\nEnter a name to look up their phone number: ")
phone_number = contact_dict.get(user_input, "Not found.")
print(f"Phone number for {user_input}: {phone_number}")



 # **Compulsory Task(but not graded): Student Profile Builder**
# - This program collects student details, academic scores, hobbies, and guardian info, stores them in a nested dictionary, and performs automatic calculations and transformations using dictionary comprehension, tuple unpacking, and set operations.

# **Requirements**

# - You are to are to study the project below, understand the thought process or flow, understand the codes and all the python components used.
# - Then let it inspire you to create something similar. You are free to be creative and adapt it to anything you wish to create.
# **My thought flow**

# 1. understanding the task
# - I want to create a program that collects student information and presents it in a clean, organized way.
# - The program should:
#   - Collect personal details (name, age, gender).
#   - Collect academic scores for a fixed set of subjects.
#   - Store guardian information.
#   - Store hobbies without duplicates.
#   - Automatically calculate average score and initials. 
 
# Student Profile Builder

# Fixed set of subjects
subjects = ("Math", "English", "Science", "History")

# Step 1: Collect personal details
name = input("Enter student's full name: ")().strip().title()
age = input("Enter student's age: ").strip()
gender = input("Enter gender: ").strip().upper()

# Step 2: Collect scores (dictionary comprehension + validation)
scores = {
    subject: float(input(f"Enter score for {subject}: "))
    for subject in subjects
}
 
# Step 3: Calculate average score
average_score = sum(scores.values()) / len(scores)

# Step 4: Guardian info (tuple unpacking)
guardian_name, guardian_relationship, guardian_contact = (
    input("Guardian's name: ").strip().title(),
    input("Relationship to student: ").strip().title(),
    input("Contact number: ").strip()
)

# Step 5: Hobbies (set to remove duplicates)
hobbies_input = input("Enter hobbies (comma-separated): ").split(",")
hobbies = {hobby.strip().title() for hobby in hobbies_input if hobby.strip()}

# Step 6: Initials
initials = "".join(word[0].upper() for word in name.split())

# Step 7: Build nested dictionary
student_profile = {
    "personal_details": {
        "name": name,
        "initials": initials,
        "age": age,
        "gender": gender
    },
    "academic_scores": scores,
    "average_score": average_score,
    "guardian_info": {
        "name": guardian_name,
        "relationship": guardian_relationship,
        "contact": guardian_contact
    },
    "hobbies": hobbies
}

# Step 8: Display neatly
print("\n--- STUDENT PROFILE ---")
print(f"Name: {student_profile['personal_details']['name']} ({student_profile['personal_details']['initials']})")
print(f"Age: {student_profile['personal_details']['age']}")
print(f"Gender: {student_profile['personal_details']['gender']}\n")

print("Academic Scores:")
for subject, score in student_profile["academic_scores"].items():
    print(f"  {subject}: {score}")

print(f"Average Score: {student_profile['average_score']:.2f}\n")

print("Guardian Information:")
for key, value in student_profile["guardian_info"].items():
    print(f"  {key.capitalize()}: {value}")

print("\nHobbies:", ", ".join(student_profile["hobbies"]))










# ---------------------------
# Student Profile Builder
# ---------------------------

# Step 1: Predefined subjects (tuple - fixed set)
subjects = ("Math", "English", "Science", "History")

# Step 2: Initialize nested dictionary structure
student_profile = {
    "personal_details": {},
    "academic_scores": {},
    "average_score": 0.0,
    "guardian_info": {},
    "hobbies": set()
}

# Step 3: Collect Personal Details
name = input("Enter student's full name: ").strip().title()
while not name:
    print("Name cannot be empty.")
    name = input("Enter student's full name: ").strip().title()

age = input("Enter student's age: ").strip()
while not age.isdigit():
    print("Age must be a number.")
    age = input("Enter student's age: ").strip()

gender = input("Enter gender (M/F/O): ").strip().upper()
while gender not in ("M", "F", "O"):
    print("Invalid input. Enter M, F, or O.")
    gender = input("Enter gender (M/F/O): ").strip().upper()

# Generate initials automatically
initials = "".join(word[0].upper() for word in name.split())

student_profile["personal_details"] = {
    "name": name,
    "initials": initials,
    "age": int(age),
    "gender": gender
}

# Step 4: Collect Academic Scores
for subject in subjects:
    score = input(f"Enter score for {subject}: ").strip()
    while not score.replace('.', '', 1).isdigit():
        print("Score must be a number.")
        score = input(f"Enter score for {subject}: ").strip()
    student_profile["academic_scores"][subject] = float(score)

# Calculate average score
student_profile["average_score"] = sum(student_profile["academic_scores"].values()) / len(subjects)

# Step 5: Collect Guardian Info
guardian_name = input("Enter guardian's full name: ").strip().title()
while not guardian_name:
    print("Guardian name cannot be empty.")
    guardian_name = input("Enter guardian's full name: ").strip().title()

guardian_relationship = input("Enter relationship to student: ").strip().title()
while not guardian_relationship:
    print("Relationship cannot be empty.")
    guardian_relationship = input("Enter relationship to student: ").strip().title()

guardian_contact = input("Enter guardian's contact number: ").strip()
while not guardian_contact.isdigit():
    print("Contact number must contain only digits.")
    guardian_contact = input("Enter guardian's contact number: ").strip()

student_profile["guardian_info"] = {
    "name": guardian_name,
    "relationship": guardian_relationship,
    "contact": guardian_contact
}

# Step 6: Collect Hobbies (No duplicates)
hobbies_input = input("Enter hobbies (comma-separated): ").split(",")
cleaned_hobbies = {h.strip().title() for h in hobbies_input if h.strip()}
student_profile["hobbies"] = cleaned_hobbies

# Step 7: Display Profile Neatly
print("\n--- STUDENT PROFILE ---")
print(f"Name: {student_profile['personal_details']['name']} ({student_profile['personal_details']['initials']})")
print(f"Age: {student_profile['personal_details']['age']}")
print(f"Gender: {student_profile['personal_details']['gender']}\n")

print("Academic Scores:")
for subject, score in student_profile["academic_scores"].items():
    print(f"  {subject}: {score}")
print(f"Average Score: {student_profile['average_score']:.2f}\n")

print("Guardian Information:")
for key, value in student_profile["guardian_info"].items():
    print(f"  {key.capitalize()}: {value}")

