
from Post import Post

class SalePost(Post):
    def __init__(self, user, type, product, price, location):
        self.product = product
        self.price = price
        self.location = location
        self.available = True
        super().__init__(user, type)

    def discount(self, discount, password):
        if self.owner.password == password:
            self.price *= (100-discount)/100.0
            print("Discount on "+self.owner.username+" product! the new price is: " + str(self.price))

    def sold(self, password):
        if self.owner.password == password and self.available:
            self.available = False
            print(self.owner.username + "'s product is sold")

    def __str__(self):
        return self.owner.username + " posted a product for sale:\nFor sale! " + self.product + ", price: " + str(self.price) + ", pickup from: " + self.location + "\n"