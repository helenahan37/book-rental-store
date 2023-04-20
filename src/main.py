# The program should present the customer with a list of services to choose from: 1. Borrow a book, 2. Return a book, 3. Quit.

# If the customer selects "Borrow a book," the program should print out a list of available books, books information, their due dates, rating starts and whether they are available for rental. 
# The program should then collect the customer's information and print a receipt that includes the customer's name,
# the date the book was borrowed, the due date, and the deposit amount.

# If the customer selects "Return a book," the program should prompt the customer to enter the receipt number for the book being returned. The program should then print out the amount due for the book and refund the deposit.
# when customer returned a book, the program should ask customer wether they want rate the book, and update the book rate information

# if customer rate the book, the program should calculate the new book rate and update the book rate information

# if customer don't rate the book, the program should print a message to tell customer they can rate the book later and quit the program 


import datetime
from prettytable import PrettyTable
import re


# define a book list dictionary
books = [
    {"id": "001", "name": "Python Crash Course", "author": "Eric Matthes", "rental_price": 17.90, "status": "available", "due_date": None, "book_rate": 4.8, "receipt_number": "None"},
    {"id": "002", "name": "Web Scraping with Python", "author": "Ryan Mitchell", "rental_price": 19.00, "status": "unavailable", "due_date": "2023-04-22", "book_rate": 4.5, "receipt_number": 10},
    {"id": "003", "name": "Python Data Science Handbook", "author": "Jake VanderPlas", "rental_price": 22.0, "status": "available", "due_date": None, "book_rate": 4.3, "receipt_number": "None"},
    {"id": "004", "name": "Expert Python Programming", "author": "Tarek Ziade", "rental_price": 15.70, "status": "available", "due_date": None, "book_rate": 3.8, "receipt_number": "None"},
    {"id": "005", "name": "Python Network Programming", "author": "Dr. M. O. Faruque Sarker", "rental_price": 23.50, "status": "unavailable", "due_date": "2023-04-23", "book_rate": 4.0, "receipt_number": 11}
]

# change the due date and receipt number manually input from string to date format
for book in books:
    if book ["due_date"] != None:
        book ["due_date"] = datetime.datetime.strptime(book ["due_date"], "%Y-%m-%d").date()
    
# obtain current date
now = datetime.datetime.now()


# calculate the due date
booked_due_date = now.date() + datetime.timedelta(days=7)


#Regex

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
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
    table = PrettyTable(["ID", "Name", "Author", "Rental Price", "Status", "Due Date", "Book Rate", "Receipt Number"])
    for book in books:
        row=[book["id"], book["name"], book["author"], book["rental_price"], book["status"], book["due_date"], book["book_rate"], book["receipt_number"]]
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
            print("\nSorry, the book ID you have entered is not valid, please enter a valid 3-digit integer ID.")
        else:
            break
    
    # create a selected_book dictionary to store the selected book
    selected_book = {}
    for book in books:
            if book["id"] == book_id:
                selected_book = book
                break 
    if not selected_book:
        print("\nSorry, the book ID you have entered is not list in our online store. If you would like to add a new book, please press option 3.")
        return None
    
    elif selected_book["status"] == "unavailable":
        booked_due_date = selected_book["due_date"]
        available_days = booked_due_date - now.date()
     
        print(f"\nSorry, the book is unavailable for rental currently. It will be available from {selected_book['due_date']}, {available_days.days} days from today.")  
        return None

    return selected_book        

# ================================ Borrow book function ==============================================


# define a function enable users to reiterate the book list
def browse_books():
    while True:
        confirm_browse = input("\nDo you want to continue to browse our book list? (y/n): ").lower()
        if confirm_browse not in ["y", "n"]:
            print("\nSorry, the option you have entered is not valid, please enter 'y' or 'n'.")
        elif confirm_browse == "y":
            display_books(books)
            choose_book = select_book(books)
            if choose_book != None:
                borrow_book(choose_book, choose_book["id"])
                return True
        else:
            print("\nThank you for using our online book rental service. See you next time!")
            break     
       
# define a receipt number
receipt_count = 11
def generate_receipt_number():
    global receipt_count
    receipt_count += 1
    return receipt_count

def borrow_book(selected_book, book_id):
# This function updates the information of the selected book and
# print a receipt number for the transaction.
    continue_borrowing = True
    while continue_borrowing and selected_book["status"] == "available":
        confirm_borrow = input("\nThe book is currently available, do you want to borrow this book? (y/n): ").lower()   
        if confirm_borrow not in ["y", "n"]:
            print("\nSorry, the option you have entered is not valid, please enter 'y' or 'n'.")
        elif confirm_borrow == "y":
            print ("\nPlease enter your personal information to complete the transaction.")
            name = validate_name()
            address = validate_address()
            email =validate_email()
            phone = validate_phone()
            # create a receipt dictionary to store the receipt information
            receipts = {}
            receipts = [{"name": name, "address": address, "phone": phone, "email": email, "book_id": book_id, "book_name": selected_book["name"], "borrow_date": now.date(), "due_date": booked_due_date, "deposit": round(selected_book["rental_price"] * 0.2, 2)}]
            print(f"\nThank you for borrowing {selected_book['name']}. Here is your receipt.")

            # create a table to display receipt information
            receipts_table = PrettyTable()
            receipt_num = generate_receipt_number()
            receipts_table.field_names = [f"Receipt Number: {receipt_num}", "Information"]
            for receipt in receipts:
                receipts_table.add_row(["Name:", receipt["name"]])
                receipts_table.add_row(["Address:", receipt["address"]])
                receipts_table.add_row(["Phone:", receipt["phone"]])
                receipts_table.add_row(["Email:", receipt["email"]])
                receipts_table.add_row(["Book ID:", receipt["book_id"]])
                receipts_table.add_row(["Book Name:", receipt["book_name"]])
                receipts_table.add_row(["Borrow Date:", receipt["borrow_date"]])
                receipts_table.add_row(["Due Date:", receipt["due_date"]])
                receipts_table.add_row(["Deposit:", receipt["deposit"]])
            print(receipts_table.get_string())

            # update the selected book status and due date
            selected_book["status"] = "unavailable"
            selected_book["due_date"] = booked_due_date
            selected_book["receipt_number"] = receipt_num
            return receipt_num
        else:
            continue_borrowing = browse_books()
            break
            
    
  

# ===================================Return Book Function===============================================================

def return_book(books):

#This function asks the user to input the receipt number to return the book, 
# and also prompts them to rate the book they borrowed. Additionally, 
# it can display a table showing the deposit paid and the remaining balance that the client needs to pay for the book.

    while True:
        try:
            return_receipt_number = int(input("\nPlease enter your receipt number: "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    for book in books:
        if book["receipt_number"] == return_receipt_number:
            print(f"\nThank you for returning {book['name']}.")
            
        # validate the book rate
            while True:
                try:
                    current_book_rate = float(input("\nPlease rate the book you have borrowed: "))
                    if current_book_rate <= 0 or current_book_rate > 5:
                        raise ValueError
                except ValueError as e:
                    print(e)
                    print(type(e))
                    print("\nInvalid input. Please enter a non-zero number (from 1-5)")
                    
                else:     
                    # update the book info
                    average_rate = (book["book_rate"] + current_book_rate)/2
                    book["book_rate"] = float(format(average_rate, '.1f'))
                    book["status"] = "available"
                    book["due_date"] = None
                    book["receipt_number"] = None
                    print(f"\nThank you for updating {book['name']}'s rate!")

                    # calculate the due balance table
                    due_balance = book["rental_price"] - book["rental_price"] * 0.2
                    deposit =book["rental_price"] * 0.2
                    print(f"\nPlease pay your due balance: ${due_balance:.2f}")
                    due_balance_table = PrettyTable(["Receipt Number", "Rental Price", "Deposit", "Due Balance"])
                    due_balance_table.add_row([return_receipt_number, book["rental_price"], f"{deposit:.2f}", "{:.2f}".format(due_balance)])
                    print(due_balance_table)
                    return book
    print("\nThe number you entered is not in the list. Please check your receipt for correct receipt number!")

    return None
        
# =============================================Add Book Function===============================================================

    
while True:
    print("\nWelcome to our online book rental service. Please choose your service type:")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Add a wish list book")
    print("4. Exit the program")

    # obtain user input1
    choice = input("\nPlease enter your choice: ")
    
    if choice == '1':
        display_books(books)
        selected_book = select_book(books)
        if selected_book != None:
            borrow_book(selected_book, selected_book["id"])
            
            
    # obtain user input2
    elif choice == '2':
        display_books(books)
        returned_book_list= return_book(books)
        if returned_book_list != None:
            print("\nUpdated book list:")
            display_books(books)
            print("\nThank you for using our online book rental service. Have a nice day!")
     
    

       

            
        