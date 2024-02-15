
from Post import Post

class TextPost(Post):
    def __init__(self, user, type, text):
        super().__init__(user, type)
        self.text = text
        print(user.username + ' published a post:\n"' + text + '"\n')