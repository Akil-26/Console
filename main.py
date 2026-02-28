from services.bookstore import Bookstore

def menu():
    store = Bookstore()
    while True:
        print("Welcome to the Book Store!")
        print("1. View all books")
        print("2. Add a new book")
        print("3. Buy a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            store.view_books()
        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            store.add_book(title, author)
        elif choice == '3':
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter book ID to buy: "))
            store.buy_book(user_id, book_id)
        elif choice == '5':
            print("Thank you for visiting the Book Store!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()