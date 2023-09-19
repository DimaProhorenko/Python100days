size = input("Enter pizza size: ")
add_pepperoni = input("Add pepperoni (y, n): ")
add_cheese = input("Add cheese (y, n): ")
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3


if add_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
