print("Welcome to the Rollercoaster")
height = float(input("Enter your height: "))

if height >= 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your ticket is $5.")
    elif age > 12 and age <= 18:
        print("Your ticket is $7.")
    else:
        print("Your ticket is $12")
else:
    print("You can't ride")
