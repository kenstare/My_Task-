def check_scholarship_eligibility(citizenship, enrollment, other_scholarship, waec_grades):
    """
    Checks if an applicant meets the Federal Government Scholarship eligibility requirements.

    Parameters:
    citizenship (str): Applicant's citizenship.
    enrollment (bool): True if applicant is a registered, full-time undergraduate in a Nigerian university.
    other_scholarship (bool): True if applicant is currently receiving another Oil & Gas scholarship.
    waec_grades (dict): Dictionary of WAEC/WASSCE subjects and grades.

    Returns:
    bool: True if eligible, False otherwise.
    """
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
    required_subjects = ["English", "Mathematics"]
    distinction_count = 0
    for subject, grade in waec_grades.items():
        if grade in ["A", "B"]:
            distinction_count += 1

    # Must have at least 5 distinctions including English and Mathematics
    if distinction_count < 5:
        return False
    for subject in required_subjects:
        if waec_grades.get(subject) not in ["A", "B"]:
            return False

    return True

# Example usage:
# Applicant details
citizenship = input("Enter your citizenship: ")
enrollment = input("Are you a registered, full-time undergraduate in a Nigerian university? (yes/no): ").lower() == "yes"
other_scholarship = input("Are you currently receiving any Oil & Gas scholarship? (yes/no): ").lower() == "yes"
waec_grades = {}
print("Enter your WAEC/WASSCE grades for 5 subjects (A/B/C/D/E/F):")
for subject in ["English", "Mathematics", "Physics", "Chemistry", "Biology"]:
    grade = input(f"{subject}: ").upper()
    waec_grades[subject] = grade

if check_scholarship_eligibility(citizenship, enrollment, other_scholarship, waec_grades):
    print("You are eligible for the Federal Government Scholarship.")
else:
    print("You are NOT eligible for the Federal Government Scholarship.")


   