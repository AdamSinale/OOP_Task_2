
from User import User

class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.users = []
            self.logged_in = []
            self.logged_out = []
            print("The social network " + name + " was created!")
            self.initialized = True

    def sign_up(self, userName, password):
        user = User(userName, password)
        self.users.append(user)
        self.logged_in.append(user)
        return user

    def log_in(self, userName, password):
        for user in self.logged_out:
            if user.username == userName and user.password == password:
                self.logged_out.remove(user)
                self.logged_in.append(user)
                print(userName + " connected")

    def log_out(self, userName):
        for user in self.logged_in:
            if user.username == userName:
                self.logged_out.append(user)
                self.logged_in.remove(user)
                print(userName + " disconnected")

    def __str__(self):
        str = self.name + " social network:\n"
        for user in self.users:
            str += user.__str__() + "\n"
        return str