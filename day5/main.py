from lib2to3.pygram import Symbols
import numbers
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)


for char in range(1, nr_symbols + 1):
     password_list += random.choice(Symbols)



for char in range(1, nr_numbers + 1):
     password_list += random.choice(numbers)


random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")    
