print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
name1 = "Catherine Zeta-Jones"
name2 = "Michael Douglas"

count1 = 0
count2 = 0

combined_name = name1.lower() + name2.lower()
check_word = "true"
check_word2 = "love"

for letter in check_word:
    count1 += combined_name.count(letter)
for letter in check_word2:
    count2 += combined_name.count(letter)

score = int(str(count1) + str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
