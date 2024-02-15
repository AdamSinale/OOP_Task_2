
from Post import Post

class ImagePost(Post):
    def __init__(self, user, type, imageURL):
        super().__init__(user, type)
        self.imageURL = imageURL
        print(user.username + " posted a picture\n")

    def display(self):
        print("Shows picture")