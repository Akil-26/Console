import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv('host')
        self.user = os.getenv('user')
        self.password = os.getenv('password')   
        self.database = os.getenv('database')
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Database connection successful.")
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query):
        if not self.connection:
            print("No database connection.")
            return None
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return False