# 写一个网上租书店的终端小程序，程序需要包含3个特色，
# The program should present the customer with a list of services to choose from: 1. Borrow a book, 2. Return a book, 3. Quit.
# If the customer selects "Borrow a book," the program should print out a list of available books, their due dates, and whether they are available for rental. The program should then collect the customer's information and print a receipt that includes the customer's name,
# the date the book was borrowed, the due date, and the deposit amount.
# If the customer selects "Return a book," the program should prompt the customer to enter the receipt number for the book being returned. The program should then print out the amount due for the book and refund the deposit.


import datetime
from prettytable import PrettyTable

# define a book list dictionary
books = [
    {"id": "001", "name": "Python Crash Course", "author": "Eric Matthes", "price": 49.9, "status": "available", "due_date": None},
    {"id": "002", "name": "Web Scraping with Python", "author": "Ryan Mitchell", "price": 69.9, "status": "unavailable", "due_date": "2022-04-20"},
    {"id": "003", "name": "Python Data Science Handbook", "author": "Jake VanderPlas", "price": 99.0, "status": "available", "due_date": None},
    {"id": "004", "name": "Expert Python Programming", "author": "Tarek Ziade", "price": 79.0, "status": "available", "due_date": None},
    {"id": "005", "name": "Python Network Programming", "author": "Dr. M. O. Faruque Sarker", "price": 59.9, "status": "unavailable", "due_date": "2022-04-22"}
]


# define a receipt list
receipts = {}

# obtain current date
now = datetime.datetime.now()

# define a table to display book list
table = PrettyTable(["ID", "Name", "Author", "Price", "Status", "Due Date"])

while True:
    print("\nWelcome to our online book rental service. Please choose your service type:")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Exit the program")

    # obtain user input1
    choice = input("Please enter your choice: ")
    
    if choice == '1':
        for book in books:
            row=[book["id"], book["name"], book["author"], book["price"], book["status"], book["due_date"]]
            table.add_row(row)
        print("\nHere is the list of books for rental: ")
        print(table)
