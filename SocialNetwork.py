
from User import User

class SocialNetwork:

    def __init__(self, name):
        self.name = name
        self.users = []
        self.logged_in = []
        self.logged_out = []
        print("The social network " + name + " was created!")

    def sign_up(self, userName, password):
        user = User(userName, password)
        self.users.append(user)
        self.logged_in.append(user)
        return user

    def log_in(self, userName, password):
        for user in self.logged_out:
            if user.name == userName and user.password == password:
                self.logged_out.remove(user)
                self.logged_in.append(user)
                print(userName + " connected")

    def log_out(self, userName):
        for user in self.logged_in:
            if user.name == userName:
                self.logged_out.append(user)
                self.logged_in.remove(user)
                print(userName + " disconnected")