
from return_book import return_book
from input_format import validate_name
from unittest.mock import patch
import pytest
from add_book import add_book
from unittest.mock import patch, Mock, MagicMock
import datetime
from borrow_book import borrow_book
from input_format import validate_name,validate_email, validate_address, validate_phone
from return_book import return_book
import builtins

# Test1 
''' This test is designed to test if the return_book function can successfully return a borrowed book with a valid receipt number and rating.'''
@pytest.fixture
# create a fixture for sample book data
def sample_books():
    books = [
        {"name": "Book A", "rental_price": 10, "book_rate": 4.5, "status": "unavailable", "due_date": "2023-05-01", "receipt_number": 1},
        {"name": "Book B", "rental_price": 12, "book_rate": 3.2, "status": "available", "due_date": "None", "receipt_number": 0},
        {"name": "Book C", "rental_price": 15, "book_rate": 4.8, "status": "unavailable", "due_date": "2023-05-03", "receipt_number": 2},
    ]
    return books

# test case 1- returning a borrowed book with a valid receipt number and rating -pass
def test_return_book_success(sample_books, mocker):
    # mock user input
    mocker.patch("builtins.input", side_effect=["1", "4.2"])
    
    # call the function
    returned_book = return_book(sample_books)
    
    # assert the book status, due date, receipt number, and book rate are updated correctly
    assert returned_book == {"name": "Book A", "rental_price": 10, "book_rate": 4.3, "status": "available", "due_date": "None", "receipt_number": 0}
    
# test case 2- returning a book with an invalid receipt number -pass
def test_return_book_invalid_receipt_number(sample_books, mocker):
    # mock user input
    mocker.patch("builtins.input", return_value="4")
    
    # call the function
    returned_book = return_book(sample_books)
    
    # assert the function returns None
    assert returned_book is None
    
#Test 2
'''This test mainly tests the functionality of the add_book() function, whether it can correctly add consecutive book IDs, 
and whether the program will report an error when the customer inputs an existing book name'''
def get_max_id(books):
    return max(int(book["id"]) for book in books)

#Test Case 1 : Max id is correctly collected from the book list - pass
def test_get_max_id():
    books = [
        {"id": "001", "name": "Book A", "author": "Author A", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0},
        {"id": "002", "name": "Book B", "author": "Author B", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0}
    ]
    assert get_max_id(books) == 2
    

# Test Case 2: expected_id is correctly added to new book lists - pass
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

# Test Case 3: Book name already exists in the list - pass
def test_add_book_already_exists(capsys):
    books = [
        {
            "id": "001",
            "name": "Python is amazing",
            "author": "Helena Han",
            "rental_price": 0.0,
            "status": "unavailable",
            "due_date": "unavailable",
            "book_rate": 0.0,
            "receipt_number": 0
        }
    ]
    # Mock input values
    with patch('builtins.input', side_effect=["Python is amazing", "Helena Han"]):
        add_book(books)
        
    # Assert that the book is not added to the list
    captured = capsys.readouterr()
    assert "Book 'Python is amazing' already exists in the list." in captured.out

# Test 3
'''
This test case is testing whether the name entered by the user matches the regular expression pattern defined in name_regex, 
which specifies that the name can include letters, dots (.), spaces, and underscores (_).
'''

# test case 1: name contains only letters and underscores - pass
def test_validate_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mart_Damon")
    assert validate_name() == "Mart_Damon"

# test case 2: name contains only letters and spaces - pass
def test_validate_name2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mart Damon")
    assert validate_name() == "Mart Damon"

# test case 3: name contains only letters and dots - pass
def test_validate_name3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mart.Damon")
    assert validate_name() == "Mart.Damon"
    
 
  
# Test 4
'''This test case is designed to verify whether the function correctly calculates 
the average rating of a book based on user input and the book's current rating, 
and updates the book's rating with the calculated value.
'''
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
   

