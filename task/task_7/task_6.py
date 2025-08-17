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
subjects = ("Math", "English", "Science", "History")

# Step 1: Collect personal details
name = input("Enter student's full name: ").strip().title()
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
