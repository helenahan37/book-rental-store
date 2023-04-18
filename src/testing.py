# import datetime
# from prettytable import PrettyTable
# import re
# import uuid

# class BookStore:
    
#     def __init__(self):
#         self.books = [
#             {"id": "001", "name": "Python Crash Course", "author": "Eric Matthes", "rental_price": 19.90, "status": "available", "due_date": None, "book_rate": 4.8, "receipt_number": "None"},
#             {"id": "002", "name": "Web Scraping with Python", "author": "Ryan Mitchell", "rental_price": 19.00, "status": "unavailable", "due_date": "2023-04-22", "book_rate": 4.5, "receipt_number": 56},
#             {"id": "003", "name": "Python Data Science Handbook", "author": "Jake VanderPlas", "rental_price": 22.0, "status": "available", "due_date": None, "book_rate": 4.3, "receipt_number": "None"},
#             {"id": "004", "name": "Expert Python Programming", "author": "Tarek Ziade", "rental_price": 15.90, "status": "available", "due_date": None, "book_rate": 3.8, "receipt_number": "None"},
#             {"id": "005", "name": "Python Network Programming", "author": "Dr. M. O. Faruque Sarker", "rental_price": 23.50, "status": "unavailable", "due_date": "2023-04-23", "book_rate": 4.0, "receipt_number": 37}
#         ]

#         self.now = datetime.datetime.now()

#         # change the due date manually input from string to date
#         for book in self.books:
#             if book ["due_date"]:
#                 book ["due_date"] = datetime.datetime.strptime(book ["due_date"], "%Y-%m-%d").date()

#         # email and phone regex
#         self.email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        
#     def validate_email(self):
#         while True:
#             email = input("Email: ")
#             if not self.email_regex.match(email):
#                 print("Sorry, the email address you have entered is not valid, please try again, format: (username)@(domainname).(top-leveldomain).")
#             else:
#                 return email

#     def display_books(self):
#         # define a table to display book list 
#         table = PrettyTable(["ID", "Name", "Author", "Rental Price", "Status", "Due Date", "Book Rate", "Receipt Number"])
#         for book in self.books:
#             row=[book["id"], book["name"], book["author"], book["rental_price"], book["status"], book["due_date"], book["book_rate"], book["receipt_number"]]
#             table.add_row(row)
#         print("\nHere is the list of books for rental: ")
#         print(table)

#     def selected_book(self, book_id):
#         # create a selected_book dictionary to store the selected book
#         selected_book = {}
#         for book in self.books:
#             if book["id"] == book_id:
#                 selected_book = book
#             break
#         return selected_book
    
# class Book:
#     def __init__(self, id, name, author, rental_price, status="available", due_date=None):
#         self.id = id
#         self.name = name
#         self.author = author
#         self.rental_price = rental_price
#         self.status = status
#         self.due_date = due_date
    
#     def __str__(self):
#         return f"Book ID: {self.id}, Book Name: {self.name}, Author: {self.author}, Rental Price: {self.rental_price}, Status: {self.status}, Due Date: {self.due_date}"

# class Receipt:
#     def __init__(self, name, address, phone, email, book_id, book_name, borrow_date, due_date, deposit, receipt_number):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.email = email
#         self.book_id = book_id
#         self.book_name = book_name
#         self.borrow_date = borrow_date
#         self.due_date = due_date
#         self.deposit = deposit
#         self.receipt_number = receipt_number
    
#     def __str__(self):
#         return f"Receipt Number: {self.receipt_number}, Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}, Book ID: {self.book_id}, Book Name: {self.book_name}, Borrow Date: {self.borrow_date}, Due Date: {self.due_date}, Deposit: {self.deposit}"

# class BookRentalService:
#     def __init__(self, books):
#         self.books = books
#         self.receipts = []
    
#     def display_books(self):
#         # create a table to display the books
#         books_table = PrettyTable()
#         books_table.field_names = ["ID", "Name", "Author", "Rental Price", "Status"]
#         for book in self.books:
#             books_table.add_row([book.id, book.name, book.author, book.rental_price, book.status])
#         print(books_table)

#     def select_book(self):
#         # obtain user input2
#         book_id = input("\nPlease enter the ID of the book you want to rent: ")
#         now = datetime.now()
        
#         # check if the book is available for rental
#         for book in self.books:
#             if book.id == book_id:
#                 if book.status == "available":
#                     booked_due_date = now.date() + timedelta(days=14)
#                     book.status = "unavailable"
#                     book.due_date = booked_due_date
#                     book.receipt_number = int(str(uuid.uuid4().hex)[:2])
#                     selected_book = book.__dict__
#                     selected_book["due_date"] = str(selected_book["due_date"])
#                     print(f"\nYou have selected {selected_book['name']}. The rental price is {selected_book['rental_price']}. You need to pay a deposit of {selected_book['rental_price']*0.2}. The book is due on {selected_book['due_date']}.")
#                     return selected_book
#                 else:
#                     booked_due_date = book.due_date
#                     available_days = booked_due_date - now.date()
#                     print(f"\nSorry, the book is unavailable for rental currently. It will be available from {book.due_date}, {available_days.days} days from today.")
#                     return None

#     def borrow_book(self, selected_book):
#         # obtain user input3
#         confirm_borrow = input("\nThe book is currently available, do you want to borrow this book? (y/n): ")
#         if confirm_borrow == "y":
#             print("\nPlease enter your information: ")
#             name = input("Name: ")
#             address = input("Address: ")
#             phone = input("Phone: ")
#             email = self.validate_email()
#             deposit = selected_book["rental_price"]*0.2
#             # create a receipt dictionary to store the receipt information
#             receipts = {}
#             receipts = [{"name": name, "address": address, "phone": phone, "email": email, "book_id": selected_book["id"], "book_name": selected_book["name"], "borrow_date": now.date(), "due_date": booked_due_date, "deposit": selected_book["rental_price"]*0.2}]
#             print(f"\nThank you for borrowing {selected_book['name']}. Here is your receipt.")
            
#             # create a table to display receipt information
#             receipts_table = PrettyTable()
#             receipts_table.field_names = [f"Receipt Number: {book.receipt_number}", "Information"]
#             for receipt in receipts:
#                 receipts_table.add_row(["Name:", receipt["name"]])
#                 receipts_table.add_row(["Address:", receipt["address"]])
#                 receipts_table.add_row(["Phone:", receipt["phone"]])
#                 receipts_table.add_row(["Email:", receipt["email"]])
#                 receipts_table.add_row(["Book ID:", receipt["book_id"]])
#                 receipts_table.add_row(["Book Name:", receipt["book_name"]])
#                 receipts_table.add_row(["Borrow Date:", receipt["borrow_date"]])
#                 receipts_table.add_row(["Due Date:", receipt["due_date"]])
#                 receipts_table.add_row(["Deposit:", receipt["deposit"]])
#             print(receipts_table.get_string())

#             # update the selected book status and due date
#             selected_book["status"] = "unavailable"
#             selected_book["due_date"] = booked_due_date
#             selected_book["receipt_number"] = book.receipt_number
            
#         else:
#             return None

#         return selected_book
    
                
# while True:
#     print("\nWelcome to our online book rental service. Please choose your service type:")
#     print("1. Borrow a book")
#     print("2. Return a book")
#     print("3. Add a wish list book")
#     print("4. Exit the program")

#     # obtain user input1
#     choice = input("Please enter your choice: ")
    
#     if choice == '1':
#         display_books(books)
#         selected_book_info = selected_book(books)
#         if selected_book_info != None:
#             borrow_book(selected_book_info, selected_book_info["id"])
    
