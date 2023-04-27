import datetime
from colored import fg, bg, attr


from input_format import validate_name,validate_email, validate_address, validate_phone
from receipt_table import generate_receipt_number, show_receipt
from prompt_yes_no import prompt_yes_or_no


def borrow_book(selected_book):
    # This function updates the information of the selected book and
    # print a receipt number for the transaction.

    if prompt_yes_or_no(f"\n{fg(229)}The book is currently available, do you want to borrow this book? (y/n): {attr(0)}"):

        print(f"\n{fg(122)}Please enter your personal information to complete the transaction.{attr(0)}")

        name = validate_name()
        address = validate_address()
        email = validate_email()
        phone = validate_phone()
        receipt_id = selected_book["id"]
        # create a receipt dictionary to store the receipt information
        # print(selected_book)

        now = datetime.datetime.now()

        receipt_num = generate_receipt_number()
        rental_price = selected_book["rental_price"]
        deposit = round(rental_price * 0.2, 2)
        
        receipt = {
            'receipt_num': receipt_num,
            "name": name,
            "address": address,
            "phone": phone,
            "email": email,
            "book_id": receipt_id,
            "book_name": selected_book["name"],
            "borrow_date": now.date(),
            "due_date": now.date() + datetime.timedelta(days=7),
            "deposit": deposit,
        }
        print(f"\n{fg(216)}{attr('bold')}Thank you for borrowing {selected_book['name']}. Here is your receipt. {attr('reset')}") 

        # create a table to display receipt information
        show_receipt(receipt)

        # update the selected book status and due date
        selected_book["status"] = "unavailable"
        selected_book["due_date"] = (now.date() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        selected_book["receipt_number"] = receipt_num

        return selected_book


