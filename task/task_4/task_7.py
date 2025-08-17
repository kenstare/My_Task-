# **Task 7: List Manipulation**
# - Create a list of five cities.
# - Replace the third city with a new one (entered by the user).
# - Remove the last city.
# - Add a new city to the beginning of the list.
# - Print the updated list.

cities = ["Ekiti", "Lagos", "Ogun", "Oyo", "Uyo"]
new_city = input("Enter a new city to replace the third city: ")
cities[2] = new_city
cities.pop()
cities.insert(0, "Ondo")
print("Updated list of cities:")
for city in cities:
    print(city)