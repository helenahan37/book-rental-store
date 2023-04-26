import csv

csv_file = 'db.csv'

# check if csv file exists

try: 
    db_file = open(csv_file, 'r')
    db_file.close()
    pass
except FileNotFoundError:
    db_file.open(csv_file, 'w')
    db_file.close()
    print("file not found, creating new file...")

def read_db(csv_file):
    books = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for book in reader:
            book["rental_price"] = float(book["rental_price"])
            book["book_rate"] = float(book["book_rate"])
            book["receipt_number"] = int(book["receipt_number"])
            books.append(book)
    return books


def write_db(books, csv_file):
    with open(csv_file, "w", newline="") as f:
        columns = ["id", "name", "author", "rental_price",
                   "status", "due_date", "book_rate", "receipt_number"]
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(books)


