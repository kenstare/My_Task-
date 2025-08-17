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

