from services.auth import Auth
from services.bookstore import Bookstore
from database import Database
auth = Auth()
store = Bookstore()
Database()
print("Welcome to the Bookstore Management System!")
while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        auth.register()
    elif choice == "2":
        user = auth.login()
        if user:
            while True:

                print(f"\nWelcome {user['name']} ({user['role']})")
                print("-" * 30)
                
                if user["role"] == "admin":
                    print("1. View Books")
                    print("2. Add Book")
                    print("3. Logout")
                else:
                    print("1. View Books")
                    print("2. Buy Book")
                    print("3. View My Orders")
                    print("4. Logout")
                

                sub_choice = input("Enter choice: ")
                
                if user["role"] == "admin":
                    
                    if sub_choice == "1":
                        store.view_books()
                    
                    elif sub_choice == "2":
                        store.add_book(user)
                    
                    elif sub_choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice, try again.")
                
                else:

                    if sub_choice == "1":
                        store.view_books()

                    elif sub_choice == "2":
                        try:
                            book_id = int(input("Enter book ID to buy: "))
                            quantity = int(input("Enter quantity: "))
                        except ValueError:
                            print("Invalid input. Please enter valid numbers.")
                            continue
                        store.buy_book(user["id"], book_id, quantity)

                    elif sub_choice == "3":
                        store.view_orders(user["id"])
                
                    elif sub_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice, try again.")

    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice, try again.")

auth.db.close()
store.db.close()