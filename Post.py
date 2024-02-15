
class Post:

    def __init__(self, owner, type):
        self.owner = owner
        self.type = type
        self.likes = set()
        self.comments = []
        print(self)

    def like(self, user):
        if user not in self.likes:
            self.likes.add(user)
            print("notification to "+self.owner.username+": "+user.username+" liked your post")

    def comment(self, sender, comment):
        self.comments.append({"sender": sender, "comment": comment})
        print("notification to "+self.owner.username+": "+sender.username+" commented on your post: "+comment)
