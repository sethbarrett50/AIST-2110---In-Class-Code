# # In Class Examples | Week 5 | AIST 2110 | Conditional Execution Cont.

# # Review


# num_votes = int(input("Enter the number of votes: "))
# num_voters = int(input("Enter the number of voters: "))
# if num_votes > num_voters / 2:
#     print("The candidate wins!")
# else:
#     print("The candidate loses.")
# input()  # Wait

# candA_votes = int(input("Enter the number of votes for Candidate A: "))
# candB_votes = int(input("Enter the number of votes for Candidate B: "))
# candC_votes = int(input("Enter the number of votes for Candidate C: "))
# num_voters = candA_votes + candB_votes + candC_votes

# if candA_votes > num_voters / 2:
#     print("Candidate A wins!")
# elif candB_votes > num_voters / 2:
#     print("Candidate B wins!")
# elif candC_votes > num_voters / 2:
#     print("Candidate C wins!")

# print("Uh what happens now?")

# if candA_votes > candB_votes and candA_votes > candC_votes:
#     print("Candidate A wins!")
# elif candB_votes > candA_votes and candB_votes > candC_votes:
#     print("Candidate B wins!")
# elif candC_votes > candA_votes and candC_votes > candB_votes:
#     print("Candidate C wins!")
# else:
#     print("It's a tie!")
#     if candA_votes == candB_votes and candA_votes == candC_votes:
#         print("Between All Candidates")
#     elif candA_votes == candB_votes:
#         print("Between Candidates A and B")
#     elif candA_votes == candC_votes:
#         print("Between Candidates A and C")
#     elif candB_votes == candC_votes:
#         print("Between Candidates B and C")


# # # AND & OR


# temperature = 75
# is_raining = False

# if temperature > 70 and not is_raining:
#     print("It's warm and dry, perfect for going outside!")
# elif temperature > 70 and is_raining:
#     print("It's warm but raining — maybe bring an umbrella.")
# elif temperature <= 70 or is_raining:
#     print("Might be too cold or wet, better stay inside.")
# else:
#     print("Conditions are uncertain, decide for yourself.")


# # # Boolean Truth Tables

# # #
# # # | A     | B     | C     | A and B | (A and B) or C |
# # # | ----- | ----- | ----- | ------- | -------------- |
# # # | True  | True  | True  | True    | True           |
# # # | True  | True  | False | True    | True           |
# # # | True  | False | True  | False   | True           |
# # # | True  | False | False | False   | False          |
# # # | False | True  | True  | False   | True           |
# # # | False | True  | False | False   | False          |
# # # | False | False | True  | False   | True           |
# # # | False | False | False | False   | False          |

# A, B, C = True, False, True  # explain multiple variable assignment on 1 line
# print(A and B)        # False
# print(A or B)         # True
# print((A and B) or C)  # True  (and happens first, then or)


# # # ## Try-Except Practice

# # try:
# #     whole_num = int(input("Enter a whole number: "))
# # except ValueError:
# #     print("That's not a valid whole number!")
# #     exit()

# try:
#     decimal_num = float(input("Enter a decimal number: "))  # Ctrl + C
#     div = decimal_num / 0
# except ValueError:
#     print("That's not a valid whole number!")
#     exit()
# except ZeroDivisionError:
#     print("You can't divide by zero!")
#     exit()
# input()
# Use REPL to show different errors


# Movie Theatre Practice

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
# -Use this format: `f"Your ticket price is: ${price}"`
#


try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
    exit()

# Add lower() & strip() example time-provided
day = input("Enter the day of the week: ")

if age < 5:
    price = 0
    print("toddlers watch for free")
elif age < 18:
    if day == "wednesday" or day == "Wednesday":
        price = 5
        print("teen discount day")
    else:
        price = 7
elif age >= 65:
    if day == "monday" or day == "Monday":
        price = 4
        print("senior Monday special")
    else:
        price = 6
else:
    if day == "tuesday" or day == "Tuesday":
        price = 8
        print("adult Tuesday discount")
    else:
        price = 10

print(f"Your ticket price is: ${price}")


# ## Math Review


# Lemonade Stand
# Reviews +, -, *, / with a tiny real-world scenario.

cups_sold = int(input("Cups sold today: "))
price_per_cup = float(input("Price per cup ($): "))

lemons_cost = float(input("Cost of lemons ($): "))
sugar_cost = float(input("Cost of sugar ($): "))
cups_cost = float(input("Cost of cups ($): "))
stand_fee = float(input("Stand/permit fee ($): "))

# *  multiplication: revenue = units * price
revenue = cups_sold * price_per_cup

# +  addition: total costs = sum of all cost items
total_costs = lemons_cost + sugar_cost + cups_cost + stand_fee

# -  subtraction: profit = revenue - costs
profit = revenue - total_costs

# /  division: average profit per cup
avg_profit = profit / cups_sold if cups_sold > 0 else 0.0

print("\n=== Lemonade Stand Summary ===")
print(f"Revenue:       ${revenue:.2f}")  # Cover .2f formatting
print(f"Total costs:   ${total_costs:.2f}")
print(f"Profit:        ${profit:.2f}")
print(f"Avg per cup:   ${avg_profit:.2f}")


# Created by Seth Barrett | 2025
