from database import Database
class Bookstore:
    def __init__(self):
        self.db = Database()
    def add_book(self, user):
        if user["role"] != "admin":
            print("Only admins can add books.")
            return
        
        print("\n--- Add Book ---")
        title = input("Title: ")
        author = input("Author: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        query = """INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)"""
        
        success = self.db.execute(query, (title, author, price, stock))

        if not success:
            print(f"Failed to add book '{title}'.")
        else:
            print(f"Book '{title}' added successfully.")
    
    def view_books(self):
        print("\n--- Available Books ---")
        query = "SELECT * FROM books"
        books = self.db.execute(query, fetch=True)
        if not books:
            print("No books available.")
            return  
        for book in books:
            print(f"""
ID: {book['id']},
Title: {book['title']},
Author: {book['author']},
Price: ${book['price']},
Stock: {book['stock']}
------------------------
""")
            if book["stock"] < 5:
                print("⚠ Low Stock Warning!\n")

    def buy_book(self, user_id, book_id, quantity=1):

        # Get book details
        query = "SELECT price, stock FROM books WHERE id = %s"
        result = self.db.execute(query, (book_id,), fetch=True)

        if not result:
            print("Book not found ❌")
            return

        book = result[0]
        price = book["price"]
        stock = book["stock"]

        if stock < quantity:
            print("Not enough stock ❌")
            return

        total_price = price * quantity

        # Reduce stock
        update_query = "UPDATE books SET stock = stock - %s WHERE id = %s"
        self.db.execute(update_query, (quantity, book_id))

        # Insert order
        order_query = """
        INSERT INTO orders (user_id, book_id, quantity, total_price)
        VALUES (%s, %s, %s, %s)
        """
        success = self.db.execute(order_query, (user_id, book_id, quantity, total_price))

        if success:
            print("Order placed successfully 📦")
        else:
            print("Failed to place order ❌")

        
    def view_orders(self,user_id):
        query = """
        SELECT books.title, orders.quantity, orders.total_price, orders.order_date
        FROM orders
        JOIN books ON orders.book_id = books.id
        WHERE orders.user_id = %s   
        """
        
        orders = self.db.execute(query,(user_id,),fetch=True)
        if not orders:
            print("No orders found.")
            return
        
        print("\n--- Your Orders ---")
        
        for order in orders:
            print(f"""
Title: {order['title']},
Quantity: {order['quantity']},
Total Price: ${order['total_price']},
Order Date: {order['order_date']}""")
print("---------------------------")