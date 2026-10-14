
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product:", self.name)


class Laptop(Product):
    def get_info(self):
        print("Laptop:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


class Mobile(Product):
    def get_info(self):
        print("Mobile:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


product1 = Laptop("Dell Laptop", 50000, "Computer")
product2 = Mobile("Samsung Mobile", 25000, "Phone")

products = [product1, product2]

for product in products:
    product.get_info()
    print()
