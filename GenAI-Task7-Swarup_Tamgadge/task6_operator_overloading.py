
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return (
            "Product(" + self.name + ", "
            + str(self.price) + ", "
            + self.category + ")"
        )

    def __add__(self, other):
        return self.price + other.price


product1 = Product("Laptop", 50000, "Electronics")
product2 = Product("Mobile", 20000, "Electronics")

print(product1)
print(product2)

total_price = product1 + product2

print("Combined Price:", total_price)

