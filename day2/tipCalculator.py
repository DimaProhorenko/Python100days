totalBill = float(input("Enter bill: "))
tip = int(input("Enter tip %: "))
peopleCount = int(input("Enter how many people to split between: "))

calculatedTip = totalBill / 100 * tip
totalBill += calculatedTip
result = round(totalBill / peopleCount)
print(f"Each person should pay: {result}")

# 17.79
