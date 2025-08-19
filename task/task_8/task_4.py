# Task4: Student Record
# - Create an empty dictionary called student.
# - Ask the user to input their name and age, then store them in the dictionary.
# - Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
# - Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
# - Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
# - Print out the complete record in this format:

# Student Record:
# Name: John
# Age: 16
# Scores: [70, 85, 90]
# Passed: True
Teenager: True

# Task4: Student Record

# Create an empty dictionary for the student
student = {}

# Ask the user to input their name and age
student["name"] = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))

# Add a list of scores to the dictionary
student["scores"] = [70, 85, 90]

# Check if the student has passed (average score >= 50)
average_score = sum(student["scores"]) / len(student["scores"])
student["passed"] = average_score >= 50

# Check if the student is a teenager (age between 13 and 19)
student["teenager"] = student["age"] >= 13 and student["age"] <= 19

# Print out the complete record
print("Student Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Scores: {student['scores']}")
print(f"Passed: {student['passed']}")
print(f"Teenager: {student['teenager']}")
