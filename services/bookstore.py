from database import Database
class Bookstore:
    def __init__(self):
        self.db = Database()

    def add_book(self, title, author):
        query = f"INSERT INTO books (title, author, available) VALUES ('{title}', '{author}', TRUE)"
        result = self.db.execute_query(query)
        if result is False:
            print(f"Failed to add book '{title}'.")
        else:
            print(f"Book '{title}' added successfully.")
    
    def view_books(self):
        query = "SELECT * FROM books"
        results = self.db.execute_query(query)
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Available: {'Yes' if row[3] else 'No'}")


    def buy_book(self, user_id, book_id):
        query = f"SELECT available FROM books WHERE id = {book_id}"
        result = self.db.execute_query(query)

        if not result:
            print("Book not found")
            return

        book = result[0]
        available = book[0]

        if not available:
            print("Book is not available")
            return

        # Mark book as unavailable
        update_query = f"UPDATE books SET available = FALSE WHERE id = {book_id}"
        self.db.execute_query(update_query)

        # Create order
        order_query = f"INSERT INTO orders (user_id, book_id, quantity, total_price) VALUES ({user_id}, {book_id}, 1, 0)"
        result = self.db.execute_query(order_query)

        if result is False:
            print("Failed to place order.")
        else:
            print("Order placed successfully!")