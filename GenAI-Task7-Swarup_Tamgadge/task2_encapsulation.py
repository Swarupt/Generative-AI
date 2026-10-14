
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than zero.")


product1 = Product("Laptop", 50000, "Electronics")

print("Original Price:", product1.get_price())

product1.set_price(55000)
print("Updated Price:", product1.get_price())

product1.set_price(-1000)
print("Final Price:", product1.get_price())
