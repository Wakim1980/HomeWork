class Product:
    name = ""
    price = 0
    def get_total(self,units):
        return units * self.price

class Product_cart:
    cart = {}
    def Add(self,object,units):
        self.cart[object] = units

    def get_total(self):
        itog = 0
        for key, element in self.cart.items():
            itog = (key.price * element) + itog
        return itog
product1 = Product()
product2 = Product()
product1.name = "apple"
product1.price = 15
product2.name = "orang"
product2.price = 30

cart1 = Product_cart()
cart1.Add(product1, 5)
cart1.Add(product2, 5)

print(cart1.get_total())