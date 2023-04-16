# 写一个网上租书店的终端小程序，程序需要包含3个特色，
# The program should present the customer with a list of services to choose from: 1. Borrow a book, 2. Return a book, 3. Quit.
# If the customer selects "Borrow a book," the program should print out a list of available books, books information, their due dates, rating starts and whether they are available for rental. The program should then collect the customer's information and print a receipt that includes the customer's name,
# the date the book was borrowed, the due date, and the deposit amount.
# If the customer selects "Return a book," the program should prompt the customer to enter the receipt number for the book being returned. The program should then print out the amount due for the book and refund the deposit.
# when customer returned a book, the program should ask customer wether they want rate the book, and update the book rate information
# if customer rate the book, the program should calculate the new book rate and update the book rate information
# if customer don't rate the book, the program should print a message to tell customer they can rate the book later and quit the program 


import datetime
from prettytable import PrettyTable

# define a book list dictionary
books = [
    {"id": "001", "name": "Python Crash Course", "author": "Eric Matthes", "price": 49.9, "status": "available", "due_date": None, "book_rate": 4.8},
    {"id": "002", "name": "Web Scraping with Python", "author": "Ryan Mitchell", "price": 69.9, "status": "unavailable", "due_date": "2022-05-20", "book_rate": 4.5},
    {"id": "003", "name": "Python Data Science Handbook", "author": "Jake VanderPlas", "price": 99.0, "status": "available", "due_date": None, "book_rate": 4.3},
    {"id": "004", "name": "Expert Python Programming", "author": "Tarek Ziade", "price": 79.0, "status": "available", "due_date": None, "book_rate": 3.8},
    {"id": "005", "name": "Python Network Programming", "author": "Dr. M. O. Faruque Sarker", "price": 59.9, "status": "unavailable", "due_date": "2022-05-22", "book_rate": 4.0}
]


# define a receipt list
receipts = {}

# obtain current date
now = datetime.datetime.now()

# define a function to calculate the waiting date between current date and due date
booked_due_date = now.date() + datetime.timedelta(days=7)
available_days = booked_due_date - now.date()

# define a table to display book list
table = PrettyTable(["ID", "Name", "Author", "Price", "Status", "Due Date", "Book Rate"])



while True:
    print("\nWelcome to our online book rental service. Please choose your service type:")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Exit the program")

    # obtain user input1
    choice = input("Please enter your choice: ")
    
    if choice == '1':
        table.clear_rows()
        for book in books:
            row=[book["id"], book["name"], book["author"], book["price"], book["status"], book["due_date"], book["book_rate"]]
            table.add_row(row)
        print("\nHere is the list of books for rental: ")
        print(table)
        book_id = input("Please enter the book ID you want to borrow: ")
        # create a selected_book dictionary to store the selected book
        selected_book = {}
        for book in books:
            if book["id"] == book_id:
                selected_book = book
                break
            
        if not selected_book:
            print("Sorry, the book is not available in our online store. Please try again later.")

        elif selected_book["status"] == "available":
            confirm_borrow = input("Do you want to borrow this book? (y/n): ")
            if confirm_borrow == "y":
                print("Please enter your information: ")
                name = input("Name: ")
                address = input("Address: ")
                phone = input("Phone: ")
                email = input("Email: ")
                deposit = selected_book["price"]*0.2
                # create a receipt dictionary to store the receipt information
                receipts = [{"name": name, "address": address, "phone": phone, "email": email, "book_id": book_id, "book_name": selected_book["name"], "borrow_date": now.date(), "due_date": booked_due_date, "deposit": selected_book["price"]*0.2}]
                print(f"Thank you for borrowing {selected_book['name']}. Here is your receipt.")
                
                # create a table to display receipt information
                receipts_table = PrettyTable(["Name", "Address", "Phone", "Email", "Book ID", "Book Name", "Borrow Date", "Due Date", "Deposit"])
                for receipt in receipts:
                    receipts_table.add_row([receipt["name"], receipt["address"], receipt["phone"], receipt["email"], receipt["book_id"], receipt["book_name"], receipt["borrow_date"], receipt["due_date"], receipt["deposit"]])
                print(receipts_table)
                
                # update the selected book status and due date
            selected_book["status"] = "unavailable"
            selected_book["due_date"] = booked_due_date
            books.append(selected_book)
        else:
            print(f"Sorry, the book is unavailable for rental. It will be available from {selected_book['due_date']}.")

            
              