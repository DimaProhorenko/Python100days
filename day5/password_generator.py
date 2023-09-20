import random


print("Welcome to the PyPassword Generator")

num_letters = int(input("Enter number of letters: "))
num_numbers = int(input("Enter number of numbers: "))
num_symbols = int(input("Enter number of symbols: "))


password = ""

for letter in range(0, num_letters):
    rand = random.randint(65, 90)
    char = chr(rand)
    password += char if rand % 2 == 0 else char.lower()

for num in range(0, num_numbers):
    password += str(random.randint(1, 9))


for num in range(0, num_symbols):
    password += chr(random.randint(33, 47))


print("".join(random.sample(password, len(password))))
