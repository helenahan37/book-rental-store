'''This is the main program for the book rental system.

The program should present the customer with a list of services to choose from: 1. Borrow a book, 2. Return a book, 3. Quit.
If the customer selects "Borrow a book," the program should print out a list of available books, books information, their due dates, rating starts and whether they are available for rental.

The program should then collect the customer's information and print a receipt that includes the customer's name,
the date the book was borrowed, the due date, and the deposit amount.

If the customer selects "Return a book," the program should prompt the customer to enter the receipt number for the book being returned. The program should then print out the amount due for the book and refund the deposit.
when customer returned a book, the program should ask customer wether they want rate the book, and update the book rate information

if customer rate the book, the program should calculate the new book rate and update the book rate information

if customer don't rate the book, the program should print a message to tell customer they can rate the book later and quit the program
'''


import datetime
from prettytable import PrettyTable
import re
import csv
# books = [
#     {"id": "001", "name": "Python Crash Course", "author": "Eric Matthes", "rental_price": 17.90, "status": "available", "due_date": "None", "book_rate": 4.8, "receipt_number": "None"},
#     {"id": "002", "name": "Web Scraping with Python", "author": "Ryan Mitchell", "rental_price": 19.00, "status": "unavailable", "due_date": "2023-05-12", "book_rate": 4.5, "receipt_number": 10},
#     {"id": "003", "name": "Python Data Science Handbook", "author": "Jake VanderPlas", "rental_price": 22.0, "status": "available", "due_date": "None", "book_rate": 4.3, "receipt_number": "None"},
#     {"id": "004", "name": "Expert Python Programming", "author": "Tarek Ziade", "rental_price": 15.70, "status": "available", "due_date": "None", "book_rate": 3.8, "receipt_number": "None"},
#     {"id": "005", "name": "Python Network Programming", "author": "Dr. M. O. Faruque Sarker", "rental_price": 23.50, "status": "unavailable", "due_date": "2023-05-19", "book_rate": 4.0, "receipt_number": 11}
# ]
receipt_count = 20

# Regex
email_regex = re.compile(
 r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regex = re.compile(r'^0\d{9}$')
name_regex = re.compile(r'^[A-Za-z][A-Za-z_.\s]{7,29}$')
address_regex = re.compile(r'^[\d\s\w]{5,50}$')



# define a function to validate email
def validate_email():
    while True:
        email = input("Email: ")
        if not email_regex.match(email):
            print("\nSorry, the email address you have entered is not valid, please try again, format: (username)@(domainname).(top-leveldomain).")
        else:
            return email

# define a function to validate phone number


def validate_phone():
    while True:
        phone = input("Phone: ")
        if not phone_regex.match(phone):
            print("\nSorry, the phone number you have entered is not valid, please try again, format: 10-digit phone number start from 0.")
        else:
            return phone

# define a function to validate name


def validate_name():
    while True:
        name = input("Name: ")
        if not name_regex.match(name):
            print("\nSorry, the name you have entered is not valid, please try again, format: 8-30 characters, only letters, space, dot and underscore.")
        else:
            return name


def validate_address():
    while True:
        address = input("Address: ")
        if not address_regex.match(address):
            print("\nSorry, the address you have entered is not valid, please try again, format: 5-50 characters, only letters, numbers and space.")
        else:
            return address

# define a function to display book list


def display_books(books):
 # define a table to display book list
    table = PrettyTable(["ID", "Name", "Author", "Rental Price",
                        "Status", "Due Date", "Book Rate", "Receipt Number"])
    for book in books:
        row = [book["id"], book["name"], book["author"], book["rental_price"],
               book["status"], book["due_date"], book["book_rate"], book["receipt_number"]]
        table.add_row(row)
    print("\nHere is the list of books for rental: ")
    print(table)

# define a function for selected book


def select_book(books):
    # This function prompts the user to select a book from the given list of books
    # and returns the details of the selected book.
    while True:
        book_id = input("\nPlease enter the book ID you are interested: ")
        if not book_id.isdigit() or len(book_id) != 3:
            print(
                "\nSorry, the book ID you have entered is not valid, please enter a valid 3-digit integer ID.")
        else:
            break

    selected_book = [item for item in books if item["id"] == book_id]
    if len(selected_book) == 0:
        print("\nSorry, the book ID you have entered is not list in our online store. If you would like to add a new book, please press option 3.")
        return

    selected_book = selected_book[0]

    if selected_book["status"] == "unavailable":
        if selected_book["due_date"] == "unavailable":
            print(
                f"\nSorry, the book will be add to our online store later, please check it after 7 days.")
        else:
            now = datetime.datetime.now()
            time_diff = datetime.datetime.strptime(
                selected_book["due_date"], "%Y-%m-%d").date() - now.date()
            print(
                f"\nSorry, the book is unavailable for rental currently. It will be available from {selected_book['due_date']}, {time_diff.days} days from today.")
        return

    return selected_book


# ================================ Borrow book function ==============================================


# create receipt number

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


def borrow_book(selected_book):
    # This function updates the information of the selected book and
    # print a receipt number for the transaction.

    if prompt_yes_or_no("\nThe book is currently available, do you want to borrow this book? (y/n): "):

        print("\nPlease enter your personal information to complete the transaction.")

        name = validate_name()
        address = validate_address()
        email = validate_email()
        phone = validate_phone()
        receipt_id = selected_book["id"]
        # create a receipt dictionary to store the receipt information
        # print(selected_book)

        now = datetime.datetime.now()

        receipt_num = generate_receipt_number()
        receipt = {
            'receipt_num': receipt_num,
            "name": name,
            "address": address,
            "phone": phone,
            "email": email,
            "book_id": receipt_id,
            "book_name": selected_book["name"],
            "borrow_date": now.date(),
            "due_date": now.date() + datetime.timedelta(days=7),
            "deposit": round(selected_book["rental_price"] * 0.2, 2)
        }
        print(
            f"\nThank you for borrowing {selected_book['name']}. Here is your receipt.")

        # create a table to display receipt information
        show_receipt(receipt)

        # update the selected book status and due date
        selected_book["status"] = "unavailable"
        selected_book["due_date"] = (now.date() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        selected_book["receipt_number"] = receipt_num

        return selected_book


# ===================================Return Book Function===============================================================

def return_book(books):
    # This function asks the user to input the receipt number to return the book,
    # and also prompts them to rate the book they borrowed. Additionally,
    # it can display a table showing the deposit paid and the remaining balance that the client needs to pay for the book.

    while True:
        try:
            return_receipt_number = int(input("\nPlease enter your receipt number: "))
            if return_receipt_number <= 0:
                print("\nPlease enter a positive number.")
                continue
            
            for book in books:
                if book["receipt_number"] == return_receipt_number:
                    print(f"\nThank you for returning {book['name']}.")
                    while True:
                        try:
                            current_book_rate = float(input("\nPlease rate the book you have borrowed: "))       
                            if current_book_rate <= 0 or current_book_rate > 5:
                                raise ValueError
                        except ValueError:
                            print(
                                "\nInvalid input. Please enter a non-zero number (from 1-5)")
                        else:
                            if book['book_rate'] == -1:
                                average_rate = current_book_rate
                            else:
                                average_rate = (book["book_rate"] + current_book_rate)/2
                                          
                            book["book_rate"] = float(
                                format(average_rate, '.1f'))

                            book["status"] = "available"
                            book["due_date"] = "None"
                            book["receipt_number"] = "-1"

                            print(
                                f"\nThank you for updating {book['name']}'s rate!")

                            due_balance = book["rental_price"] - \
                                book["rental_price"] * 0.2
                            deposit = book["rental_price"] * 0.2
                            print(
                                f"\nPlease pay your due balance: ${due_balance:.2f}")
                            due_balance_table = PrettyTable(
                                ["Receipt Number", "Rental Price", "Deposit", "Due Balance"])
                            due_balance_table.add_row(
                                [return_receipt_number, book["rental_price"], f"{deposit:.2f}", "{:.2f}".format(due_balance)])
                            print(due_balance_table)
                            return book
            else:
                print( "\nThe number you entered is not in the list. Please double check your receipt number.")    
                break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")


# =============================================Add Book Function===============================================================
def add_book(books):
    print("\nPlease enter the following information to add a book:")

    # add id from book list

    max_id = max(int(book["id"]) for book in books)

    # create a new book dictionary
    new_book = {}
    new_book["id"] = str(max_id + 1).zfill(3)
    new_book["name"] = input("Book Name: ")
    new_book["author"] = input("Author: ")
    new_book["rental_price"] = -1
    new_book["status"] = "unavailable"
    new_book["due_date"] = "unavailable"
    new_book["book_rate"] = -1
    new_book["receipt_number"] = -1

    books.append(new_book)

    return books

csv_file = 'db.csv'

# check if csv file exists

try: 
    db_file = open(csv_file, 'r')
    db_file.close()
    print("Database file found.")
except FileNotFoundError:
    db_file.open(csv_file, 'w')
    db_file.close()
    print("file not found, creating new file...")

def read_db(csv_file):
    books = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for book in reader:
            book["rental_price"] = float(book["rental_price"])
            book["book_rate"] = float(book["book_rate"])
            book["receipt_number"] = int(book["receipt_number"])
            books.append(book)
    return books


def write_db(books, csv_file):
    with open(csv_file, "w", newline="") as f:
        columns = ["id", "name", "author", "rental_price",
                   "status", "due_date", "book_rate", "receipt_number"]
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(books)


def prompt_yes_or_no(prompt):
    while True:
        confirm_browse = input(prompt).lower()
        if confirm_browse not in ["y", "n"]:
            print("\nSorry, the option you have entered is not valid, please enter 'y' or 'n'.")         
        else:
            return confirm_browse == "y"

# =============================================Main Function===============================================================


def main():

    books = read_db(csv_file)

    print("\nWelcome to our online book rental service. Please choose your service type:")

    def main_menu():

        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Add a wish list book")
        print("4. Exit the program")
        choice = input("\nPlease enter your choice: ")
        return choice

    user_choice = ""

    while user_choice != "4":
        user_choice = main_menu()

        #  check the validation of user input
        if user_choice not in ["1", "2", "3", "4"]:
            print("\nInvalid input. Please enter a number from 1-4.")
            continue

        # obtain user input1
        if user_choice == "1":
            # def execute_user_choice_1(books):
            while True:
                display_books(books)
                selected_book = select_book(books)
                # if client select and confirm to borrow o book, update the book list
                if selected_book is not None:
                    if borrow_book(selected_book) is not None:
                        write_db(books, csv_file)
                if not prompt_yes_or_no("\nDo you want to continue to browse our book list? (y/n): "):
                    print("\nThank you for using our online borrow book service.")
                    break

        # obtain user input2
        elif user_choice == "2":
            while True:
                display_books(books)
                returned_book = return_book(books)
                if returned_book is not None:
                    write_db(books, csv_file)
                    print("\nUpdated book list:")
                    display_books(books)
                    print("\nThank you for using our online book return rental service.")
                    break
                else:
                    if not prompt_yes_or_no("\nDo you want to continue to return your book? (y/n): "):
                        print("\nThank you for using our online book return book service.") 
                        break

        # obtain user input3
        elif user_choice == "3":
            while True:
                display_books(books)
                add_book(books)
                write_db(books, csv_file)
                print(
                    f"\nThe book has been added to the list. It will be available in 7 days")
                display_books(books)
                if not prompt_yes_or_no("\nDo you want to continue to add new book? (y/n): "):
                    print("\nThank you for using our online adding book service.")
                    break

        elif user_choice == "4":
            write_db(books, csv_file)
            print( "\nThank you for using our online book rental service. See you next time!")           
            continue

        else:
            print("\nInvalid input. Please enter a number from 1-4.")
            continue

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
