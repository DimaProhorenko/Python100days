year = int(input("Enter year to check: "))
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 100 == 0 and year % 400 == 0:
        print("Leap year.")
else:
    print("Not leap year.")
