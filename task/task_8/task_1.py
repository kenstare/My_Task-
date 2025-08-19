# Task1
# Explain each output of the program below.
# - Give 3 usecases or cenarios where you can apply the program below.
# - Write the code for 1 of the 3 use cases

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# Checks if num1 is equal to num2. Outputs True if they are the same, otherwise False.


print(f"{num1} != {num2} : {num1 != num2}")
# Checks if num1 is not equal to num2. Outputs True if they are different, otherwise False.


print(f"{num1} > {num2} : {num1 > num2}")
# Checks if num1 is greater than num2. Outputs True if so, otherwise False.


print(f"{num1} < {num2} : {num1 < num2}")
# Checks if num1 is less than num2. Outputs True if so, otherwise False.

print(f"{num1} >= {num2} : {num1 >= num2}")
# Checks if num1 is greater than or equal to num2. Outputs True if so, otherwise False.

# Age Verification Example

user_age = int(input("Enter your age: "))
required_age = int(input("Enter required age: "))


print(f"{num1} != {num2} : {num1 != num2}")
# Checks if num1 is not equal to num2. Outputs True if they are different, otherwise False.
print(f"Eligible (age >= required): {user_age >= required_age}")
print(f"Too young (age < required): {user_age < required_age}")
print(f"Exact age match: {user_age == required_age}")