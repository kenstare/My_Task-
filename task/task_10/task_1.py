
def check_scholarship_eligibility(citizenship, enrollment, other_scholarship, waec_grades):
    """
    Checks if an applicant meets the Federal Government Scholarship eligibility requirements.
    Returns True if eligible, False otherwise.
    """
    # Semantic error handling: Ensure required subjects are present
    required_subjects = ["English", "Mathematics"]
    for subject in required_subjects:
        if subject not in waec_grades:
            print(f"Error: Missing grade for {subject}.")
            return False

    # Check citizenship
    if citizenship.lower() != "nigeria":
        return False

    # Check enrollment status
    if not enrollment:
        return False

    # Check if receiving other Oil & Gas scholarships
    if other_scholarship:
        return False

    # Check WAEC/WASSCE grades
    distinction_count = sum(1 for g in waec_grades.values() if g in ["A", "B"])
    if distinction_count < 5:
        return False
    if waec_grades["English"] not in ["A", "B"] or waec_grades["Mathematics"] not in ["A", "B"]:
        return False

    return True

# Runtime error handling for user input
try:
    citizenship = input("Enter your citizenship: ")
    enrollment = input("Are you a registered, full-time undergraduate in a Nigerian university? (yes/no): ").lower() == "yes"
    other_scholarship = input("Are you currently receiving any Oil & Gas scholarship? (yes/no): ").lower() == "yes"
    waec_grades = {}
    print("Enter your WAEC/WASSCE grades for 5 subjects (A/B/C/D/E/F):")
    for subject in ["English", "Mathematics", "Physics", "Chemistry", "Biology"]:
        grade = input(f"{subject}: ").upper()
        if grade not in ["A", "B", "C", "D", "E", "F"]:
            print(f"Error: Invalid grade '{grade}' for {subject}.")
            raise ValueError("Invalid grade entered.")
        waec_grades[subject] = grade

    if check_scholarship_eligibility(citizenship, enrollment, other_scholarship, waec_grades):
        print("You are eligible for the Federal Government Scholarship.")
    else:
        print("You are NOT eligible for the Federal Government Scholarship.")

except Exception as e:
    print(f"Runtime Error: {e}")
