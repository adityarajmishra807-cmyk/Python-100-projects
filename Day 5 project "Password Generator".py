import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
a = int(input("How many letters would you like in your password?\n"))
b = int(input(f"How many symbols would you like?\n"))
c = int(input(f"How many numbers would you like?\n"))
password1 = ""
password2 = ""
password3 = ""
for i in range(0, a):
    random_letter = random.choice(letters)
    password1 += random_letter
for i in range(0, b):
    random_number = random.choice(numbers)
    password2 += random_number
for i in range(0, c):
    random_symbol = random.choice(symbols)
    password3 += random_symbol
print(password1+password2+password3)
