from prettytable import PrettyTable
import random
import csv
from update_csv import csv_file


with open(csv_file, "r") as f:
    reader = csv.reader(f)
    existing_receipt_numbers = set([(row[-1]) for row in reader])

generated_receipt_numbers = set()

# create receipt number
def generate_receipt_number():
    min_num = 10
    max_num = 99
    while True:
        receipt_number = random.randint(min_num, max_num)
        if receipt_number not in generated_receipt_numbers and receipt_number not in existing_receipt_numbers:
            # If the receipt number is unique, add it to the set of generated numbers and return it
            generated_receipt_numbers.add(receipt_number)
            return receipt_number


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