import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# order of characters eventually randomzied

# final list to randomize for password
final_password = []

# random selection of letters
for i in range(nr_letters):
    selection = letters[random.randint(0, len(letters) - 1)]
    final_password.append(selection)

# random selection of symbols
for i in range(nr_symbols):
    selection_symbols = symbols[random.randint(0, len(symbols) - 1)]
    final_password.append(selection_symbols)

# random selection of numbers
for i in range(nr_numbers):
    selection_numbers = numbers[random.randint(0, len(numbers) - 1)]
    final_password.append(selection_numbers)

# Randomize final password list
random.shuffle(final_password)

# convert list to string
password = ''.join(final_password)
print(f"Your randomly generated password: {password}")



