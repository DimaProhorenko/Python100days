# from turtle import Turtle, Screen

# timmy = Turtle()
# screen = Screen()

# timmy.shape("turtle")
# timmy.color("coral")

# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)

# print(screen.canvwidth)

# screen.exitonclick()


from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ["Name", "Age"]
table.add_row(["Dima", 23])
table.add_row(["Nastya", 20])

table.align = "l"

print(table)
