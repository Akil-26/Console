from database import Database

class Auth:
    def __init__(self):
        self.db = Database()
    def register(self):
        print("\n--- Register ---")
        name = input("Enter name: ")
        email = input("Enter email: ")
        role = input("Enter role (admin/customer): ")

        query = """
        INSERT INTO users (name, email, role)
        VALUES (%s, %s, %s)
        """

        success = self.db.execute(query, (name, email, role))

        if success:
            print("User registered successfully ✅")
        else:
            print("Registration failed ❌")

    def login(self):
        print("\n--- Login ---")
        email = input("Enter email: ")

        query = "SELECT * FROM users WHERE email = %s"
        user = self.db.execute(query, (email,), fetch=True)

        if user:
            print("Login successful ✅")
            return user[0]   # return first match
        else:
            print("User not found ❌")
            return None