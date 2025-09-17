# Movie Theater Pricing Problem
#
# We want to take an age(whole number) and a day of the week(str) from the user
# - Use try-except to catch Value Error if invalid age is provided -> exit()
# - Make sure day of the week is stripped & capitalized
#
# Pricing Scheme:
# - Toddlers(less than 5) are free every day
# - Teens(less than 18) on Wednesday are discounted to $5; normal teen price is $7
# - Seniors(65 & older) are discounted for senior Monday special to $4; normal senior price is $6
# - Adults(all others) are discounted on Tuesday to $8; normal adult price is $10
#
# Save the price of the ticket to a price variable, and print the price at the end
# -Use this format: if the ticket is $50, print in this format: Your ticket price is: $50
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
    exit()
if age < 0:
    print("Age cannot be negative.")
    exit()
if age > 120:
    print("Age seems too high.")
    exit()
day = input("Enter day of the week: ").strip().capitalize()

if age < 5:
    price = 0
elif age < 18:
    if day == "Wednesday":
        price = 5
    else:
        price = 7
elif age >= 65:
    if day == "Monday":
        price = 4
    else:
        price = 6
else:
    if day == "Tuesday":
        price = 8
    else:
        price = 10


print(f"Your ticket price is: ${price}")
