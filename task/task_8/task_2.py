# Task2
# - Comment the code below appropriately, and using doctring, explain what the code is doing.
# -  Adapt the code to the case below.

# - Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria.
 # - Enrollment:
 #  - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
 # - Other Scholarships:
 # - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international.
 # - Academic Qualification:
 # - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

eligibility = (age < 18) and (score > 70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


# Get applicant's name
name = input("Enter your name: ")

# Get applicant's citizenship
citizenship = input("Enter your citizenship: ")

# Check enrollment status
enrollment = input("Are you a registered, full-time undergraduate in a Nigerian university? (yes/no): ").lower() == "yes"

# Check if applicant is receiving any other Oil & Gas scholarship
other_scholarship = input("Are you currently receiving any Oil & Gas scholarship? (yes/no): ").lower() == "yes"

# Collect WAEC/WASSCE grades for 5 subjects
waec_grades = {}
print("Enter your WAEC/WASSCE grades for 5 subjects (A/B/C/D/E/F):")
for subject in ["English", "Mathematics", "Physics", "Chemistry", "Biology"]:
    grade = input(f"{subject}: ").upper()
    waec_grades[subject] = grade

# Check eligibility based on requirements
distinctions = sum(1 for g in waec_grades.values() if g in ["A", "B"])
english_math_distinction = waec_grades["English"] in ["A", "B"] and waec_grades["Mathematics"] in ["A", "B"]

eligibility = (
    citizenship.lower() == "nigeria" and
    enrollment and
    not other_scholarship and
    distinctions >= 5 and
    english_math_distinction
)

# Output result
print(f"\nCandidate: {name}")
print(f"Eligible for Federal Government Scholarship: {eligibility}")