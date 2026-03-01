import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("host"),
                user=os.getenv("user"),
                password=os.getenv("password"),
                database=os.getenv("database")
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            self.connection = None

    def execute(self, query, values=None, fetch=False):
        if not self.connection:
            print("No database connection.")
            return None

        try:
            self.cursor.execute(query, values)

            if fetch:
                return self.cursor.fetchall()

            self.connection.commit()
            return True

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return False

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    db = Database()
    db.close()