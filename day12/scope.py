enemies = 1
check = [1, 2]


def increase(check):
    enemies = 2
    check = []
    print(f"Enemies inside function: {enemies}")


def bar():
    a = 9
    if 16 > 9:
        a = 16
    print(a)


# increase(check)
# print(f"Enemies outside: {enemies}")
# print(check)

bar()
