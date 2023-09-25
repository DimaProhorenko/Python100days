def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def subtract(num1, num2):
    return num1 - num2


def get_operator():
    is_oper_correct = False
    oper = ""
    print_operator()
    while not is_oper_correct:
        oper = input("Enter operation: ")
        if oper in opers:
            is_oper_correct = True
        else:
            print("Uknown operation")
    return oper


def print_operator():
    print("Enter one of the operators provided below")
    for oper in opers:
        print(oper)


def update_continue_calc(calc_result):
    is_valid = False
    result = False
    while not is_valid:
        should_continue = input(
            f"Continue calculation with {calc_result}? Type 'y' to continue, 'n' to skip: ")
        if should_continue.lower() == "y":
            is_valid = True
            result = True
        elif should_continue.lower() == "n":
            is_valid = True
            result = False

    return result


def print_calculation(n1, n2, oper, result):
    print(f"{n1} {oper} {n2} = {result}")


def remove_trailing_zero(num):
    return str(round(num, 2)).rstrip(".0")


def start():
    remember_result = False
    result = 0
    while True:
        if remember_result:
            n1 = result
        else:
            n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        oper = get_operator()

        result = opers[oper](n1, n2)
        print_calculation(n1, n2, oper, result)
        should_exit = input("Wanna exit? Type 'y' to exit, 'n' to continue: ")
        if should_exit == 'y':
            break
        should_continue = update_continue_calc(result)
        if should_continue:
            remember_result = True
        else:
            remember_result = False


opers = {
    "+": add,
    "*": multiply,
    "/": divide,
    "-": subtract
}

print("Welcome to calc.py")
start()
