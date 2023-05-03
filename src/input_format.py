import re
from colored import fg, bg, attr

# Regex
email_regex = re.compile(
 r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regex = re.compile(r'^0(?![0]{9})\d{9}$')
name_regex = re.compile(r'^[A-Za-z][A-Za-z_.\s]{5,20}[A-Za-z]$')
address_regex = re.compile(r'^[\d\s\w]{10,50}$')
book_name_regex = re.compile(r'^(?=.*[a-zA-Z0-9])[a-zA-Z0-9\s\-\.:]{5,20}$')


# define a function to validate email
def validate_email():
    while True:
        email = input("Email: ")
        if not email_regex.match(email):
            print(f"\n{fg(229)}Sorry, the email address you have entered is not valid, please try again, format: (username)@(domainname).(top-leveldomain). {attr(0)}")
        else:
            return email

# define a function to validate phone number
def validate_phone():
    while True:
        phone = input("Phone: ")
        if not phone_regex.match(phone):
            print(f"\n{fg(229)}Sorry, the phone number you have entered is not valid, please try again, format: 10-digit phone number start from 0, but cannot all 0. {attr(0)}")
        else:
            return phone

# define a function to validate name
def validate_name():
    while True:
        name = input("Name: ")
        if not name_regex.match(name):
            print(f"\n{fg(229)}Sorry, the name you have entered is not valid, please try again, format: 7-22 characters, only letters, space, dot and underscore. {attr(0)}")
        else:
            return name

 # define a function to validate address
def validate_address():
    while True:
        address = input("Address: ")
        if not address_regex.match(address):
            print(f"\n{fg(229)}Sorry, the address you have entered is not valid, please try again, format: 10-50 characters, only letters, numbers and space. {attr(0)}")
        else:
            return address
        
# define a function to validate book name
def validate_book_name():
    while True:
        book_name = input("Book Name: ")
        if not book_name_regex.match(book_name):
            print(f"\n{fg(229)}Sorry, the book name you have entered is not valid, please try again, format: 5-20 characters, only letters, space, hyphen, dot and colon. {attr(0)}")
        else:
            return book_name
        
# define a function to validate book author        
def validate_author_name():
    while True:
        book_author = input("Book Author: ")
        if not name_regex.match(book_author):
            print(f"\n{fg(229)}Sorry, the author name you have entered is not valid, please try again, format: 7-22 characters, only letters, space, dot and underscore. {attr(0)}")
        else:
            return book_author