# **Task 5: Student Score Tracker**
# - Ask the user for 3 student names.
# - For each student, ask for their score.
# - Store the results in two lists (one for names, one for scores).
# - Print a formatted output showing Name — Score, aligned neatly.
# - Tips: You are to start by creating two empty lists.

names = []
scores = []
for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    score = input(f"Enter the score of {name}: ")
    names.append(name)
    scores.append(score)

print("\nStudent Scores:")
for i in range(len(names)):
    print(f"{names[i]} — {scores[i]}")
