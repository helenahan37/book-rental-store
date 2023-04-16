# 写一个网上租书店的终端小程序，程序需要包含3个特色，
# The program should present the customer with a list of services to choose from: 1. Borrow a book, 2. Return a book, 3. Quit.
# 1. If the customer selects "Borrow a book," the program should print out a list of available books, their due dates, and whether they are available for rental. The program should then collect the customer's information and print a receipt that includes the customer's name,
# the date the book was borrowed, the due date, and the deposit amount.
# 2.If the customer selects "Return a book," the program should prompt the customer to enter the receipt number for the book being returned. The program should then print out the amount due for the book and refund the deposit.
import datetime

# define a book list
books = [
    {'id': '001', 'name': 'Python Crash Course', 'author': 'Eric Matthes', 'price': 49.9, 'status': 'available', 'due_date': None},
    {'id': '002', 'name': 'Web Scraping with Python', 'author': 'Ryan Mitchell', 'price': 69.9, 'status': 'unavailable', 'due_date': '2022-04-20'},
    {'id': '003', 'name': 'Python Data Science Handbook', 'author': 'Jake VanderPlas', 'price': 99.0, 'status': 'available', 'due_date': None},
    {'id': '004', 'name': 'Expert Python Programming', 'author': 'Tarek Ziade', 'price': 79.0, 'status': 'available', 'due_date': None},
    {'id': '005', 'name': 'Python Network Programming', 'author': 'Dr. M. O. Faruque Sarker', 'price': 59.9, 'status': 'unavailable', 'due_date': '2022-04-22'}
]


# define a receipt list
receipts = {}

# obtain current date
now = datetime.datetime.now()

while True:
    print("\nWelcome to our online book rental service. Please choose your service type:")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Exit the program")

    # obtain user input
    choice = input('请输入数字选择服务类型：')

    if choice == '1':  # 借书
        print('\n当前书籍列表如下:')

        print('编号\t书名\t\t\t\t\t作者\t\t状态\t\t可借日期')

        # 遍历书籍列表，打印书籍信息
        for book in books:
            print(f'{book["id"]}\t{book["name"]}\t\t{book["author"]}\t{book["status"]}\t{book["due_date"] or "N/A"}')

        # 获取用户输入
        book_id = input('请输入要借阅的书籍编号：')
        name = input('请输入您的姓名：')
        phone_number = input('请输入您的联系电话：')
        address = input('请输入您的家庭住址：')

        # 查找书籍信息
        book = None
        for b in books:
            if b['id'] == book_id:
                book = b
                break

        if book is None:
            print('对不起，没有找到您想借阅的书籍。')
        elif book['status'] == 'unavailable':
            due_date = datetime.datetime.strptime(book['due_date'], '%Y-%m-%d')
            days_left = (due_date - now).days
            if days_left > 0:
                print(f'对不起，该书籍于{book["due_date"]}后可借')
                
        elif book is not None and book['status'] == 'available':
    # 更新书籍状态和借出日期
            book['status'] = 'unavailable'
            book['due_date'] = (now + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

    # 生成收据编号
            receipt_id = len(receipts) + 1

    # 计算押金金额
            deposit = 0.2 * book['price']

            print('\n您已成功借阅以下书籍:')
            print(f'书籍名称：{book["name"]}')
            print(f'借出日期：{now.strftime("%Y-%m-%d")}')
            print(f'归还日期：{book["due_date"]}')
            print(f'押金金额：{deposit:.2f}元')
            
            receipts[receipt_id] = {
                'book_name': book['name'],
                'borrower_name': name,
                'phone_number': phone_number,
                'address': address,
                'borrow_date': now.strftime("%Y-%m-%d"),
                'return_date': book["due_date"],
                'deposit_amount': deposit
            }

            print('\n收据编号:', receipt_id)
            print('书籍名称：', book['name'])
            print('借阅人姓名：', name)
            print('联系电话：', phone_number)
            print('家庭住址：', address)
            print('借出日期：', now.strftime("%Y-%m-%d"))
            print('归还日期：', book["due_date"])
            print(f'押金金额：{deposit:.2f}元')
    