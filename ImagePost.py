
from Post import Post

class ImagePost(Post):
    def __init__(self, user, type, imageURL):
        self.imageURL = imageURL
        super().__init__(user, type)

    def display(self):
        print("Shows picture")

    def __str__(self):
        return self.owner.username + " posted a picture\n"