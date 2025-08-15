# **Task1: Fruit collector**
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

favourite_fruits = set()
for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    favourite_fruits.add(fruit)

print("Your favourite fruits are:")
print(favourite_fruits)

# **Task2: Unique Name Collector**
# - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

attendees = set()
while True:
    name = input("Enter attendee's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    attendees.add(name)
print(sorted(attendees))

# **Task3: Simulate a football match ticket system** 
# - Store all seat numbers (1 to 50) in a set
# - Ask users to "book" a seat by entering the number.
# - Remove booked seats from the set.
# - Show remaining seats after each booking.

seats = set(range(1, 51))
while True:
    print("Available seats:", seats)
    choice = input("Enter a seat number to book: ")
    if choice.lower() == 'exit':
        break
    if choice.isdigit():
        seat_number = int(choice)
        if seat_number in seats:
            seats.remove(seat_number)
            print(f"Seat {seat_number} booked successfully.")
        else:
            print("Invalid seat number or already booked.")
    else:
        print("Invalid input. Please enter a seat number.") 


# **Task4: Create a Unique Voters Registration System**
# - Ask for voter names and store in a set.
# - If a voter tries to register twice, display a warning.
# - After registration, display the total number of unique voters.

voters = set()
while True:
    name = input("Enter voter's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    if name in voters:
        print("This voter is already registered.")
    else:
        voters.add(name)
        print("Voter registered successfully.")

print("Total unique voters registered:", len(voters))