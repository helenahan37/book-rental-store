'''This is the main program for the book rental system.

The program should present the customer with a list of services to choose from: 1. Borrow a book, 2. Return a book, 3. Quit.
If the customer selects "Borrow a book," the program should print out a list of available books, books information, their due dates, rating starts and whether they are available for rental.

The program should then collect the customer's information and print a receipt that includes the customer's name,
the date the book was borrowed, the due date, and the deposit amount.

If the customer selects "Return a book," the program should prompt the customer to enter the receipt number for the book being returned. The program should then print out the amount due for the book and refund the deposit.
when customer returned a book, the program should ask customer wether they want rate the book, and update the book rate information

if customer rate the book, the program should calculate the new book rate and update the book rate information

if customer don't rate the book, the program should print a message to tell customer they can rate the book later and quit the program
'''

from prettytable import PrettyTable
from colored import fg, bg, attr
import sys

from return_book import return_book
from add_book import add_book
from display_books import display_books
from select_book import select_book
from borrow_book import borrow_book, prompt_yes_or_no
from update_csv import write_db, read_db, csv_file

# =============================================Main Function===============================================================
    
def main():

    books = read_db(csv_file)

    print(f"{fg('blue')}{attr('bold')}\nWelcome to our online book rental store. Please choose your service: {attr('reset')}")

    def main_menu():

        print(f"{fg(229)}\n1. Borrow a book{attr('reset')}")
        print(f"{fg(229)}2. Return a book{attr('reset')}")
        print(f"{fg(229)}3. Add a wish list book{attr('reset')}")
        print(f"{fg(229)}4. Exit the program{attr('reset')}")

        choice = input(f"{fg(122)}\nPlease enter your choice: {attr('reset')}")
        return choice

    user_choice = ""

    while user_choice != "4":
        user_choice = main_menu()

        #  check the validation of user input
        if user_choice not in ["1", "2", "3", "4"]:
            print("\nInvalid input. Please enter a number from 1-4.")
            continue

        # obtain user input1
        if user_choice == "1":
            # def execute_user_choice_1(books):
            while True:
                display_books(books)
                selected_book = select_book(books)
                # if client select and confirm to borrow o book, update the book list
                if selected_book is not None:
                    if borrow_book(selected_book) is not None:
                        write_db(books, csv_file)
                if not prompt_yes_or_no(f"\n{fg(117)}{attr('bold')}Do you want to continue to browse our book list? (y/n): {attr('reset')}"):
                    print(f"\n{fg(216)}{attr('bold')}{attr('bold')}Thank you for using our online borrow book service. {attr('reset')}")
                    break

        # obtain user input2
        elif user_choice == "2":
            while True:
                display_books(books)
                returned_book = return_book(books)
                if returned_book is not None:
                    write_db(books, csv_file)
                    print(f"{fg(229)}\nUpdated book list: {attr(0)}")
                    display_books(books)
                    print(f"{fg(216)}{attr('bold')}\nThank you for using our online book return service. {attr(0)}")
                    break
                else:
                    if not prompt_yes_or_no(f"{fg(117)}{attr('bold')}\nDo you want to continue to return your book? (y/n):  {attr(0)}"):
                        break

        # obtain user input3
        elif user_choice == "3":
            while True:
                display_books(books)
                add_book(books)
                write_db(books, csv_file)
                print(f"{fg(123)}{attr('bold')}\nThe book has been added to the list. It will be available in 7 days. {attr(0)}")
                display_books(books)
                if not prompt_yes_or_no(f"\n{fg(193)}{attr('bold')}Do you want to continue to add new book? (y/n):  {attr(0)}"):
                    print(f"\n{fg(216)}{attr('bold')}Thank you for using our online adding book service. {attr(0)}")
                    break

        elif user_choice == "4":
            write_db(books, csv_file)
            print(f"{fg(216)}{attr('bold')}\nThank you for using our online book rental store. See you next time! {attr(0)}")           
            sys.exit()

        else:
            print(f"{fg(229)}\nInvalid input. Please enter a number from 1-4. {attr(0)}")
            continue

if __name__ == "__main__":
    main()     



