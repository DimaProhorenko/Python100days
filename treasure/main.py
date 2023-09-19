import first_level

while True:
    play = input("Wanna play?(Y/N): ").lower()
    if play == "y":
        first_level.start()
    elif play == "n":
        break
