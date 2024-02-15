
from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

class User:

    def __init__(self, userName, password):
        self.username = userName
        self.password = password
        self.posts = []
        self.followers = set()

    def follow(self, user2):
        if user2 not in self.followers:
            self.followers.add(user2)
            print(self.username + " started following " + user2.username)

    def unfollow(self, user2):
        if user2 in self.followers:
            self.followers.remove(user2)

    def publish_post(self, type, *args):
        if type == "Text":
            post = TextPost(self, type, args[0])
        elif type == "Image":
            post = ImagePost(self, type, args[0])
        elif type == "Sale":
            post = SalePost(self, type, *args)
        else:
            raise ValueError("Invalid post type")

        self.posts.append(post)
        return post
