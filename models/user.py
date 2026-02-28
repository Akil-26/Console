class User:
    def __init__(self, username, role):
        self.__username = username
        self.__role = role

    def get_username(self):
        return self.__username

    def get_role(self):
        return self.__role
    def set_username(self, username):
        self.__username = username
    def set_role(self, role):
        self.__role = role
    def __str__(self):
        return f"User(username={self.__username}, role={self.__role})"
    