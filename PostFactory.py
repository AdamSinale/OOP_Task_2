
from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

class PostFactory:
    def createPost(owner, type, content, price=None, location=None):
        if type == "Text":
            return TextPost(owner, type, content)
        elif type == "Image":
            return ImagePost(owner, type, content)
        elif type == "Sale":
            return SalePost(owner, type, content, price, location)
        else:
            raise ValueError("Invalid post type")