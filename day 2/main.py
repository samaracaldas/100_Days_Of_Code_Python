#Day 2 Project: Tip Calculator

from typing import final


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

percent = tip/100
totalTip = bill * percent
totalBill = bill + totalTip
billPerPerson = totalBill / people
final_amount = round(billPerPerson, 2)
# final_amount = "{:.2f}".format(billPerPerson) --> formatação de casa decimal

print(f"Each person should pay: ${final_amount}")