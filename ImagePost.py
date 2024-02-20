import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Post import Post

class ImagePost(Post):
    def __init__(self, user, type, imageURL):
        self.imageURL = imageURL
        super().__init__(user, type)

    def display(self):
        image_data = mpimg.imread(self.imageURL)
        plt.imshow(image_data)
        plt.axis('off')
        plt.show()

    def __str__(self):
        return self.owner.username + " posted a picture\n"