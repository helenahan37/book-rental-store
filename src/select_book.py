import datetime
from colored import fg, bg, attr


# define a function for selected book
def select_book(books):
    # This function prompts the user to select a book from the given list of books
    # and returns the details of the selected book.
    while True:
        book_id = input(f"\n{fg(122)}Please enter the book ID you are interested: {attr(0)}")
        if not book_id.isdigit() or len(book_id) != 3:
            print(f"\n{fg(226)}Sorry, the book ID you have entered is not valid, please enter a valid 3-digit integer ID. {attr(0)}")         
        else:
            break

    selected_book = [item for item in books if item["id"] == book_id]
    if len(selected_book) == 0:
        print(f"\n{fg(226)}Sorry, the book ID you have entered is not list in our online store. If you would like to add a new book, please press option 3. {attr(0)}")
        return

    selected_book = selected_book[0]

    if selected_book["status"] == "unavailable":
        if selected_book["due_date"] == "unavailable":
            print(f"\n{fg(226)}Sorry, the book will be add to our online store later, please check it after 7 days.")
        else:
            now = datetime.datetime.now()
            time_diff = datetime.datetime.strptime(
                selected_book["due_date"], "%Y-%m-%d").date() - now.date()
            print(f"\n{fg(226)}Sorry, the book is unavailable for rental currently. It will be available from {selected_book['due_date']}, {time_diff.days} days from today. {attr(0)}")        
        return

    return selected_book

