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

