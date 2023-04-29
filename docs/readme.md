# T1A3 - Online Book Rental Store
---
### GitHub Repository 

**[Link to GitHub Repository](https://github.com/helenahan37/T1A3)**

***
## Main Features And Characteristics:
The Online Book Rental Store application, as the name suggests, is a convenient terminal application that allows customers to repeatedly view the book listing, rent books, return books, and add books after starting to use the application. It has the following main features and characteristics:

1. Customers can rent the books online and browse the inventory of books as a table.
2. Customers can return the books at their convenience and get a receipt and rate the book they have borrowed.
3. Customers can add new books to the store's inventory.


### Rent books:
#### Book list Table:
This feature allows users to borrow a book online, it imports the 'PrettyTable' module to create a well-organized and easily readable table to present the book information stored in a CSV document to customers (a try-except statement has been used here to check if a CSV file exists). The table is constructed using the PrettyTable function, which defines the column headers. Next, the program iterates through a list of books, appending the data of each book as a row to the table. Finally, the program prints out the entire table containing all book details, making it simple for customers to comprehend the availability of each book. 
![Book list Table](./book%20list%20table.png)

#### Borrowed receipt:
When customers viewed the book list, the select book function prompts them to enter a book ID. The program then searches the book list to determine if the book is available or not and informs the customer of their choice's availability through prompt statements. If the customer successfully chooses an available book, they can input their personal information (regex format used here) to receive a borrowed receipt. 
![book receipt](./book%20receipt.png)

If the book is not available, the program will use the imported datetime module to inform the customer of the number of days until the book becomes available again. This is done by subtracting the current date from the book's due date.
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

## Installation Guide:

To install and run this program

1. Open the terminal and create a directory or navigate to one you wish the project to go.
2. Copy the following the link ```git@github.com:helenahan37/T1A3.git``` into your terminal hit enter
3. Navigate to source file by ```cd src ```
4. This project required Python3, please check your Python version by run ```chmod +x python_version_check.sh``` and ```./python_version_check.sh``` 
5. Check venv environment by run ```chmod +x venv_check.sh``` and ```./venv_check.sh```
6. Now you can run ```./run.sh``` to start the app

## Testing Doc

The testing for this project involves a combination of manual and automated testing.

Here is some examples' of automated testing using Pytest: 

1. Testing Case 1:

This test case is testing whether the name entered by the user matches the regular expression pattern defined in name_regex, 
which specifies that the name can include letters, dots (.), spaces, and underscores (_).

```
# test case 1: name contains only letters and underscores - pass
def test_validate_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mart_Damon")
    assert validate_name() == "Mart_Damon"
```
```
# test case 2: name contains only letters and spaces - pass
def test_validate_name2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mart Damon")
    assert validate_name() == "Mart Damon
```
```
# test case 3: name contains only letters and dots - pass
def test_validate_name3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mart.Damon")
    assert validate_name() == "Mart.Damon"
```

2. Testing Case 2:

This test case is designed to verify whether the function correctly calculates 
the average rating of a book based on user input and the book's current rating, 
and updates the book's rating with the calculated value.

```
# Test Case 1: Average rate updated correctly - pass
def test_average_rate_calculation():
    # create a sample book with initial book rate
    book = {
        "name": "Python is Great",
        "author": "F. Scott Fitzgerald",
        "book_rate": 3.5,
        "status": "unavailable",
        "due_date": "2023-05-01",
        "receipt_number": 12
    }
    
    # simulate user input to rate the book
    current_book_rate = 4.0
    
    # calculate the expected average rate
    expected_average_rate = (book["book_rate"] + current_book_rate) / 2
    
    # update the book's rate with the expected average rate
    book["book_rate"] = expected_average_rate
    
    # assert that the book's rate has been updated correctly
    assert book["book_rate"] == 3.75
```
```
# Test Case 2: Average rate calculate correctly - pass
def test_average_rate_calculation2():
# create a sample book with initial book rate
    book = {
        "name": "Python is Great",
        "author": "F. Scott Fitzgerald",
        "book_rate": 3.5,
        "status": "unavailable",
        "due_date": "2023-05-01",
        "receipt_number": 12
    }

    # simulate user input to rate the book
    current_book_rate = 5

    # calculate the expected average rate
    expected_average_rate = (book["book_rate"] + current_book_rate) / 2

    # assert that the book's rate has been calculate correctly
    assert expected_average_rate == 4.25
```
Testing Case 3: 
This test case is designed to verify if the max id is correctly collected from the book list.
```
#Test Case 1 : Max id is correctly collected from the book list - pass
def test_get_max_id():
    books = [
        {"id": "001", "name": "Book A", "author": "Author A", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0},
        {"id": "002", "name": "Book B", "author": "Author B", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0}
    ]
    assert get_max_id(books) == 2
```
```    
#Test Case 2 : assert value is false, max id is not correctly collected from the book list - raise ValueError

def test_get_max_id1():
    books = [
        {"id": "001", "name": "Book A", "author": "Author A", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0},
        {"id": "002", "name": "Book B", "author": "Author B", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0}
    ]

    max_id = get_max_id(books)
    assert max_id == 3, f"Expected max_id to be 3, but got {max_id}."
    raise ValueError("Incorrect max_id value.")
```
```
# Test Case 3: expected_id is correctly added to new book lists - pass
'''This test case is designed to verify if the book id correctly +1 to the book list when add a new book.'''
def test_add_book():
    # Set up test data
    books = [
        {"id": "001", "name": "Book A", "author": "Author A", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0},
        {"id": "002", "name": "Book B", "author": "Author B", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0}
    ]
    
    # Mock input values
    mock_input = Mock(side_effect=["Test Book", "Test Author"])

    # Get the expected ID
    expected_id = str(get_max_id(books) + 1).zfill(3)

    with patch('builtins.input', mock_input):
        new_books = add_book(books)

    # Get the actual ID of the last book in the list
    actual_id = new_books[-1]["id"]

    # Assert that the new book has the expected ID
    assert actual_id == expected_id
```

---
## Code Style:
---
This program is written following the PEP 8 Python language's code style guide, using clear variable and function names, appropriate indentation and comments, and other conventions to make the code easy to read and maintain.
Please refer to the following link for more details:

**[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)**

***





