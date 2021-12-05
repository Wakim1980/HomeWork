class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total(self, unit):
        return unit * self.price


class Product_cart:
    def __init__(self):
        self.cart_ = {}
        self.itog = 0
    def add(self, object, unit):
        self.cart_[object] = unit

    def add_cart(self):
        for key, element in self.cart_.items():
            self.itog = (element * key.price) + self.itog
        return self.itog

apple = Product("aplle", 10)
lemon = Product("lemon", 40)
orang = Product("orang", 35)
cart = Product_cart()
cart.add(apple, 4)
cart.add(lemon, 3)
cart.add(orang, 2)
print(cart.add_cart())
