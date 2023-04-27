##T1A3 - Online Book Rental Store
---
####GitHub Repository 

**[Link to GitHub Repository](https://github.com/helenahan37/T1A3)**

***
###Main Features And Functions:
The online book rental store program, as its name suggests, is a convenient terminal program that allows customers to rent books, return books, and add books. It has the following main features and characteristics:

---
####Borrow Book Function:
This function allows users to borrow a book online. It first checks whether the book is available, and if so, prompts the user to enter their personal information. It then generates a receipt number and creates a dictionary to store the receipt information. The function also updates the status of the selected book and the due date. 

####Return Book Functions:

This function prompts the user to input their receipt number to return a book and also requests them to rate the book they borrowed. Additionally, it can display a table that shows the deposit paid and the remaining balance that the client needs to pay for the book.

####Add Book Functions:

This function allows the user to add a new book to the online bookstore by inputting its name and author. The function then creates a new dictionary to store the book's information and append the new book to the book's list.

#### Features:
#####Well-designed book list table

The program imports the 'PrettyTable' module to create a well-organized and easily readable table to present the book information stored in a CSV document to customers. The table is constructed using the PrettyTable function, which defines the column headers. Next, the program iterates through a list of books, appending the data of each book as a row to the table. Finally, the program prints out the entire table containing all book details, making it simple for customers to comprehend the availability of each book.


####Real-time updates information
The program allows customers to borrow, return, and add books multiple times after the start of the program. It promptly updates the book information in the CSV file and displays it to the customer.

####Book Availability Checker
The program can determine whether a selected book is available for borrowing. If the book is not available, it will inform the customer when it will become available and the number of days until then.


####Borrow Receipt
The program can print a receipt after the customer borrows a book. The receipt includes the customer's contact information, book details, deposit, as well as the borrowing and returning time.

####Due Balance Receipt
After the customer returns a book, the program will print a receipt which includes the customer's rental deposit and the remaining balance to be paid, to remind the customer to make payment.

---
####Code Style:
---
This program is written following the PEP 8 Python language's code style guide, using clear variable and function names, appropriate indentation and comments, and other conventions to make the code easy to read and maintain.
Please refer to the following link for more details:

**[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)**

***





