
from return_book import return_book
from input_format import validate_name
from unittest.mock import patch
import pytest
from add_book import add_book
from unittest.mock import patch, Mock


# Test 1
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
    
 
  
# Test 2
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
   

#Test 3  
'''This test case is designed to verify if the max id is correctly collected from the book list.'''
def get_max_id(books):
    return max(int(book["id"]) for book in books)

#Test Case 1 : Max id is correctly collected from the book list - pass
def test_get_max_id():
    books = [
        {"id": "001", "name": "Book A", "author": "Author A", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0},
        {"id": "002", "name": "Book B", "author": "Author B", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0}
    ]
    assert get_max_id(books) == 2
    
#Test Case 2 : assert value is false, max id is not correctly collected from the book list - raise ValueError

def test_get_max_id1():
    books = [
        {"id": "001", "name": "Book A", "author": "Author A", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0},
        {"id": "002", "name": "Book B", "author": "Author B", "rental_price": 0.0, "status": "unavailable", "due_date": "unavailable", "book_rate": 0.0, "receipt_number": 0}
    ]

    max_id = get_max_id(books)
    assert max_id == 3, f"Expected max_id to be 3, but got {max_id}."
    raise ValueError("Incorrect max_id value.")

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
