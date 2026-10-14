
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


product1 = Product("Laptop", 50000, "Electronics")
product2 = Product("Mobile", 20000, "Electronics")

product1.get_info()

print()

product2.get_info()


# Extra: Apply discount
def_dummy = 0
