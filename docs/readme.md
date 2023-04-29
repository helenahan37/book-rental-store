# T1A3 - Online Book Rental Store
---
### GitHub Repository 

**[Link to GitHub Repository](https://github.com/helenahan37/T1A3)**
***
### Trello Board

**[Link to Trello Board](https://trello.com/b/pEMan2li/online-book-rental-store)**
***
### Presentation

***
## Main Features And Characteristics:
The Online Book Rental Store application, as the name suggests, is a convenient terminal application that allows customers to repeatedly view the book listing, rent books, return books, and add books after starting to use the application. It has the following main features and characteristics:

1. Customers can rent the books online and browse the inventory of books as a table.
2. Customers can return the books at their convenience and get a receipt and rate the book they have borrowed.
3. Customers can add new books to the store's inventory.


### Rent books:
#### Book list Table:
This feature allows users to borrow a book online, it imports the 'PrettyTable' module to create a well-organized and easily readable table to present the book information stored in a CSV document to customers (a try-except statement has been used here to check if a CSV file exists). The table is constructed using the PrettyTable function, which defines the column headers. Next, the program iterates through a list of books, appending the data of each book as a row to the table. 

Finally, the program prints out the entire table containing all book details, making it simple for customers to comprehend the availability of each book. 
![Book list Table](./book%20list%20table.png)

#### Borrowed receipt:
When customers viewed the book list, the select book function prompts them to enter a book ID. The program then searches the book list to determine if the book is available or not and informs the customer of their choice's availability through prompt statements. 

If the customer successfully chooses an available book, they can input their personal information (regex format used here) to receive a borrowed receipt. 
![borrowed receipt](./borrowed%20receipt.png)

If the book is not available, the program will use the imported "datetime" module to inform the customer of the number of days until the book becomes available again. This is done by subtracting the current date from the book's due date.
![time checker](./time%20checker.png)

The program then updates the book list accordingly. Additionally, it uses a while loop to repeatedly ask the customer if they want to view the latest book information when borrowing, returning, or adding a book. If the customer agrees, the program displays the updated book information using the table.


### Return Books:

This feature allows users to return a book by entering its receipt number. It incorporates error handling using try-except statements to ensure a smooth user experience. The input's validity is checked by verifying that it's a positive integer and that it exists in the borrowed book list. If the input is invalid, the program prompts the user to enter a valid receipt number.

When a book with a matching receipt number is found, it is marked as "available" and the due date and receipt number are removed. The user is then asked to rate the book on a scale of 1 to 5, and the program verifies that the input is within the acceptable range. If the user enters an invalid rating, they are prompted to re-enter a valid rating.

If the rating is valid, the program calculates a new average rating for the book and updates it in the book list. Additionally, the program calculates the deposit and due balance that the user needs to pay and displays them along with the receipt of the returned book.

Overall, this feature provides a straightforward and user-friendly way for users to return books and update their ratings while ensuring the validity of the input and displaying relevant information to the user.


![return book feature](return%20book.png)

### Add books:
This feature is relatively straightforward. It allows users to add a new book to the online bookstore by entering its name and author. The "add_book" function accepts a list of books from the CSV file as input. It then creates a new dictionary for the book based on the user's input for the name and author, which is validated using regular expressions and prompt statements. Also, try-except statements to used here to catch any ValueError that may be raised when checking if the book already exists in the list. The new book's ID is added sequentially based on the current maximum value stored in the dictionary. The book's status and due date are marked as 'unavailable', which is used to determine the availability of the book when the user selects a book combined with the select book function. Other details, such as rental price, book rating, and receipt number, are not processed at this stage and are instead set to "N/A", which can be updated by the admin later. Finally, the program adds the new book information to the "books" list and returns the updated list.

![add new book](Add%20new%20book.png)

## Software Development Plan:
When choosing a programming project, my goal was to implement functions within a program that could allow for adding, removing, and manipulating list items, performing simple mathematical operations, reading/saving files and combining with nested control structures. After considering these factors, I decided to choose the online book rental store project. This idea was also approved by the educator in our class group.

The entire project is being managed and tracked through Trello. This software allows me to categorize my project into different tags based on their functionalities and features, and further subdivide them into different items. I have classified these items based on their level of importance and set estimated completion times. These details will be adjusted and updated as the program progresses.

Here is the screenshot of my Trello Board:
![Trello1](Trello1.png)
![Trello2](Trello2.png)


## Help Documentation
### Installation Guide:

To install and run this program

1. Open the terminal and create a directory or navigate to one you wish the project to go.
2. Copy the following command  ```git clone git@github.com:helenahan37/T1A3.git``` into your terminal and hit enter
3. Navigate to the source file by ```cd T1A3/src ```
4. This project required Python3, please check your Python version by run ```chmod +x python_version_check.sh``` and ```./python_version_check.sh``` 
5. Check venv environment by run ```chmod +x venv_check.sh``` and ```./venv_check.sh```
6. Now you can run ```./run.sh``` to start the app

### Dependencies:
The project requires the following dependencies, you can install all of them by run ```run.sh```
```
colored==1.4.4
iniconfig==2.0.0
mock==5.0.2
packaging==23.1
pluggy==1.0.0
prettytable==3.7.0
pytest==7.3.1
wcwidth==0.2.6
```

### System/hardware Requirements:

- 8GM of RAM or more
- macOS Ventura 13.0 or higher

## Testing Doc

The testing for this project involves a combination of manual and automated testing.

Here are some examples of automated testing using pyTest: 

[test_case.py](../src/test_case.py)
## Manual Testing Ledger:
**[Link to Manual Testing Ledger](https://docs.google.com/spreadsheets/d/1Spjjr21O0xiv_KOr_VqqY-MLBG3ZR-DYsB5CUbTipL8/edit#gid=0)**

![Manual test screenshot](./manual%20test.png)
![Manual test screenshot2](./manual%20test2.png)


---
## Code Style:
---
This program is written following the PEP 8 Python language's code style guide, using clear variable and function names, appropriate indentation and comments, and other conventions to make the code easy to read and maintain.
Please refer to the following link for more details:

**[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)**

***

## Reference:

Kutaj, P. Simulating Single and Multiple Inputs using PyTest and Monkeypatch. *Search Medium*. Retrieved April 26, 2023, from https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9

Malik, U. (2021, June 8). Python: Validate Email Address with Regular Expressions (Regex). *StackAbuse*. https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/

CodingNConcepts. Java Regex to Validate Phone Number. Retrieved April 17, 2023, from https://codingnconcepts.com/java/java-regex-to-validate-phone-number/#regex-to-match-10-digit-phone-number-with-no-space

Python RegEx. *W3Schools*. Retrieved April 16, 2023, from https://www.w3schools.com/python/python_regex.asp

Detect Python version in shell script. *Stack Overflow* Retrieved April 23, 2023, from https://stackoverflow.com/questions/6141581/detect-python-version-in-shell-script


System Requirements. *TechTerms*. Retrieved April 28, 2023, from https://techterms.com/definition/system_requirements






