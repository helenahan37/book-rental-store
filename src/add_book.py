
from colored import fg, bg, attr

from input_format import validate_book_name, validate_author_name
# =============================================Add Book Function===============================================================
def add_book(books):
    print(f"\n{fg(122)}Please enter the following information to add a book: {attr(0)}")

    # add id from book list

    max_id = max(int(book["id"]) for book in books)

    book_name = validate_book_name()
    book_author = validate_author_name()
    # create a new book dictionary
    new_book = {}
    new_book["id"] = str(max_id + 1).zfill(3)
    new_book["name"] = book_name
    new_book["author"] = book_author
    new_book["rental_price"] = 0.0
    new_book["status"] = "unavailable"
    new_book["due_date"] = "unavailable"
    new_book["book_rate"] = 0.0
    new_book["receipt_number"] = 0

    books.append(new_book)
    print(f"{fg(123)}{attr('bold')}\n{book_name} has been added to the list and will become available in 7 days.{attr(0)}")

    return books