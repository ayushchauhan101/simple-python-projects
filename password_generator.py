import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

size_letters = int(input("How many letters would you like in your password?\n"))
size_symbols = int(input(f"How many symbols would you like?\n"))
size_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for char in range(0, size_letters):
    password += random.choice(letters)

for char in range(0, size_symbols):
    password += random.choice(symbols)

for char in range(0, size_numbers):
    password += random.choice(numbers)

random.shuffle(password)
print(f"your new password is:", end=" ")
for x in password:
    print(x, end="")
