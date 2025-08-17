# **Task3: Days and Activities Pairing**
# - Store days of the week in a tuple and ask the user to input an activity for three specific days.
#   - Use dictionary comprehension to pair days and activities.
#   - Print the dictionary.

# - Requirements:
#   - Use a tuple for days.
#   - Use {day: activity for day, activity in `zip(..., ...)`}.
#   - Tip: Research on how to use `zip()`

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
