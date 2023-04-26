from prettytable import PrettyTable
from colored import fg, bg, attr

# create receipt number
receipt_count = 20
def generate_receipt_number():
    global receipt_count
    receipt_count += 1
    return receipt_count


# define a receipt table
def show_receipt(receipt):
    receipt_table = PrettyTable()
    receipt_table.field_names = [f"Receipt Number: {receipt['receipt_num']}", "Information"]
    receipt_table.add_row(["Name:", receipt["name"]])
    receipt_table.add_row(["Address:", receipt["address"]])
    receipt_table.add_row(["Phone:", receipt["phone"]])
    receipt_table.add_row(["Email:", receipt["email"]])
    receipt_table.add_row(["Book ID:", receipt["book_id"]])
    receipt_table.add_row(["Book Name:", receipt["book_name"]])
    receipt_table.add_row(["Borrow Date:", receipt["borrow_date"]])
    receipt_table.add_row(["Due Date:", receipt["due_date"]])
    receipt_table.add_row(["Deposit:", receipt["deposit"]])
    print(receipt_table)