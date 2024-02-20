
from PostFactory import PostFactory
from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

class User:

    def __init__(self, userName, password):
        self.username = userName
        self.password = password
        self.posts = []
        self.notifications = []
        self.followers = set()

    def follow(self, user2):
        if self not in user2.followers:
            user2.followers.add(self)
            print(self.username + " started following " + user2.username)

    def unfollow(self, user2):
        if self in user2.followers:
            user2.followers.remove(self)
            print(self.username + " unfollowed " + user2.username)

    def publish_post(self, type, content, price=None, location=None):
        post = PostFactory.createPost(self, type, content, price, location)
        self.posts.append(post)

        for follower in self.followers:
            follower.notifications.append(self.username + " has a new post")
        return post

    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def __str__(self):
        return "User name: " + self.username + ", Number of posts: " + str(len(self.posts)) + ", Number of followers: " + str(len(self.followers))
