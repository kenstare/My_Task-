# **Task6: Attendance Tracker**
# - Write a Python program that;
# - Stores the days of the week in a tuple.
# - Stores the months of the year in another tuple.
# - Asks the user to enter:
#   - Student’s name
#   - Gender
#   - Course Track
#   - Current month number (1-12)
#   - Current day number (1-7)

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

student_name = input("Enter student's name: ")
gender = input("Enter gender: ")
course_track = input("Enter course track: ")
current_month = int(input("Enter current month number (1-12): "))
current_day = int(input("Enter current day number (1-7): "))