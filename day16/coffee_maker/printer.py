from prettytable import PrettyTable


class Printer:
    table = PrettyTable()
    table.align = "l"

    @staticmethod
    def set_fields(fields: list):
        Printer.table.field_names = fields

    @staticmethod
    def add_row(row: list):
        Printer.table.add_row(row)

    @staticmethod
    def clear_table():
        Printer.table.clear()

    @staticmethod
    def print_table():
        print(Printer.table)
