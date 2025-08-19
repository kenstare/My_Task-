# Python Operators
# Comparison Operators
a = 10
b = 20
print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 10)   # True
print(a <= 25)   # True

# Use case Example- Student Exam Result

score = 75

print(score >= 50)  # True (Passed)
print(score < 50)   # False (Failed)
print(score == 100) # False (Not full marks)


# Assignment Operators
x = 10
print("Initial value:", x)
# Initial value: 10


x += 5
print("After x += 5:", x)
# After x += 5: 15


x -= 2
print("After x -= 2:", x)
# After x -= 2: 13

x *= 3
print("After x *= 3:", x)
# After x *= 3: 39


x /= 4
print("After x /= 4:", x)
# After x /= 4: 9.75

x %= 3
print("After x %= 3:", x)
# After x %= 3: 0.75

x = 4
x **= 2
print("After x **= 2:", x)
# After x **= 2: 16

x //= 3
print("After x //= 3:", x)
# After x //= 3: 5

# Use case Example:

# Define variables
balance = 1000
deposit = 200
withdraw = 150


balance += deposit   # Add deposit
balance -= withdraw  # Subtract withdrawal

print("Updated Balance:", balance)  
# Output: Updated Balance: 1050


#Logical Operators

x = 10
y = 20

# and operator
print(x > 5 and y > 15)  # True

# or operator
print(x < 5 or y > 15)   # True

# not operator
print(not(x == 10))      # False

# Use case example1 - Scholarship Eligibility

#Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)  
# Output: Scholarship Eligible: True

# Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)  
# Output: Access Granted: True (because age < 25 even without ticket)

