
from prettytable import PrettyTable
from colored import fg, bg, attr
# ===================================Return Book Function===============================================================
def return_book(books):
    # This function asks the user to input the receipt number to return the book,
    # and also prompts them to rate the book they borrowed. Additionally,
    # it can display a table showing the deposit paid and the remaining balance that the client needs to pay for the book.

    while True:
        try:
            return_receipt_number = int(input(f"\n{fg(122)}Please enter your receipt number:  {attr(0)}"))
            if return_receipt_number <= 0:
                print(f"\n{fg(229)}Please enter a positive number. {attr(0)}")
                continue
            
            for book in books:  
                if book["receipt_number"] == int(return_receipt_number):
                    print(f"\n{fg(226)}Thank you for returning {book['name']}. {attr(0)}")
                    while True:
                        try:
                            current_book_rate = float(input(f"\n{fg(122)}Please rate the book you have borrowed:  {attr(0)}"))       
                            if current_book_rate <= 0 or current_book_rate > 5:
                                raise ValueError
                        except ValueError:
                            print(f"\n{fg(229)}Invalid input. Please enter a non-zero number (from 1-5)")
                        else:
                            average_rate = (book["book_rate"] + current_book_rate)/2
                                          
                            book["book_rate"] = float(format(average_rate, '.1f'))
                            book["status"] = "available"
                            book["due_date"] = "None"
                            book["receipt_number"] = 0

                            print(f"\n{fg(216)}{attr('bold')}Thank you for updating {book['name']}'s rate! {attr(0)}")
                        
                            due_balance = float(book["rental_price"] -  book["rental_price"] * 0.2)
                            deposit = float(book["rental_price"] * 0.2)
                            print(f"{fg(229)}\nPlease pay your due balance: ${due_balance:.2f} {attr(0)}")    
                            due_balance_table = PrettyTable(
                                ["Receipt Number", "Rental Price", "Deposit", "Due Balance"])
                            due_balance_table.add_row(
                                [return_receipt_number, book["rental_price"], f"{deposit:.2f}", "{:.2f}".format(due_balance)])
                            print(due_balance_table)
                            return book
            else:
                print(f"{fg(229)}\nThe number you entered is not in the list. Please double check your receipt number. {attr(0)}")    
                break
        except ValueError:
            print(f"{fg(229)}\nInvalid input. Please enter a valid number. {attr(0)}")

