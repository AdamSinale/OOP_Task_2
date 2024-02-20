
class Post:

    def __init__(self, owner, type):
        self.owner = owner
        self.type = type
        print(self)

    def like(self, user):
        if user not in self.owner.notifications and user != self.owner:
            notif = user.username+" liked your post"
            self.owner.notifications.append(notif)
            print("notification to "+self.owner.username+": "+notif)

    def comment(self, sender, comment):
        notif = sender.username+" commented on your post"
        self.owner.notifications.append(notif)
        print("notification to "+self.owner.username+": "+notif+": "+comment)
