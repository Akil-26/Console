class Book:
    def __init__(self, id, title, author, price):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__price = price

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price
    def set_id(self, id):
        self.__id = id
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_price(self, price):
        self.__price = price
    def __str__(self):
        return f"Book[ID={self.__id}, Title='{self.__title}', Author='{self.__author}', Price={self.__price}]"