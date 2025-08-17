# **Task2: Unique Name Collector**
# - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

attendees = set()
while True:
    name = input("Enter attendee's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    attendees.add(name)
print(sorted(attendees))
