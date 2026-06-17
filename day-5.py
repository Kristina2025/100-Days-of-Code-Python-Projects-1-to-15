import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

password_options = ["letters", "digits", "symbols"]
password = []

print("Welcome to the PyPassword Generator!")
nr_letters = input("How many letters would you like in your password?\n")
while not nr_letters.isnumeric():
    print("Please enter a valid number of letters.\n")
    nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input(f"How many symbols would you like?\n")
while not nr_symbols.isnumeric():
    print("Please enter a valid number of symbols.\n")
    nr_symbols = input(f"How many symbols would you like?\n")
nr_numbers = input(f"How many numbers would you like?\n")
while not nr_numbers.isnumeric():
    print("Please enter a valid number of numbers.")
    nr_numbers = input(f"How many numbers would you like?\n")
nr_letters, nr_symbols, nr_numbers = int(nr_letters), int(nr_symbols), int(nr_numbers)

for _ in range(0, nr_letters):
    password.append(random.choice(letters))
for _ in range(0, nr_symbols):
    password.append(random.choice(symbols))
for _ in range(0, nr_numbers):
    password.append(random.choice(digits))

random.shuffle(password)
password = "".join(password)

print(f"Your password is:\n{password}")
