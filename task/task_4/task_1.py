#**Task1: Your Favorite Life Quote**
# - Ask the user to input their favorite quote.
# - Convert it to title case.
# - Print it with quotation marks using escape sequences.

quote = input("Enter your favorite quote: ")
quote_title_case = quote.title()
print(f"Your favorite quote is: \"{quote_title_case}\"")
