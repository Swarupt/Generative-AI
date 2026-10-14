
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("Warranty:", self.warranty_years, "years")


product1 = ElectronicProduct(
    "Laptop", 50000, "Electronics", 2
)

product1.get_info()
