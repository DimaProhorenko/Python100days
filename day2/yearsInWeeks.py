age = int(input("Enter your age: \n"))

ageInDays = age * 365
ageInWeeks = age * 52
ageInMonths = age * 12

totalDays = 90 * 365
totalWeeks = 90 * 52
totalMonths = 90 * 12

print(f"You have {totalDays - ageInDays} days, {totalWeeks - ageInWeeks} weeks, {totalMonths - ageInMonths} months left")
