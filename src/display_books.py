
from prettytable import PrettyTable
from colored import fg, bg, attr

# define a function to display book list
def display_books(books):
 # define a table to display book list
    table = PrettyTable(["ID", "Name", "Author", "Rental Price",
                        "Status", "Due Date", "Book Rate", "Receipt Number"])
    for book in books:
        row = [book["id"], book["name"], book["author"], book["rental_price"],
               book["status"], book["due_date"], book["book_rate"], book["receipt_number"]]
        table.add_row(row)
        for row in table._rows:
            for i, cell in enumerate(row):
                if cell == 0:
                    row[i] = "N/A"
    print(f"{fg('cyan')}{attr('bold')}\nHere is the list of books for rental: {attr('reset')}")
    print(table)