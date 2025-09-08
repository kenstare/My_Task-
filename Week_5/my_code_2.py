"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""

def slicer_email(email):
    # split the email into username and domain
    try:
        username, domain = email.split("@")
        return username, domain
    except:
        return None, None
    # get email for the user
email = input("Enter your email address: ")
username, domain = slicer_email(email)

if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")


#
# Create an empty list to store tasks
tasks = []
# Add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')
# Remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")
# Show all tasks in the list
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")
    else:
        print("No tasks in your list!")
# Keep the program running until the user chooses to exit
while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        new_task = input("Enter the task: ")
        add_task(new_task)
    elif choice == '2':
        task_to_remove = input("Enter the task to remove: ")
        remove_task(task_to_remove)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Goodbye! Stay organized!")
        break
    else:
        print("Invalid choice. Please try again.")





