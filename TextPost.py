
from Post import Post

class TextPost(Post):
    def __init__(self, user, type, text):
        self.text = text
        super().__init__(user, type)

    def __str__(self):
        return self.owner.username + ' published a post:\n"' + self.text + '"\n'