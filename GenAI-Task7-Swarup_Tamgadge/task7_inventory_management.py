
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    # Magic method to combine prices of two products
    def __add__(self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to inventory.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Removed {name} from inventory.")
                return

        print(f"Product {name} not found.")

    def get_total_value(self):
        total = 0.0

        for product in self.products:
            total = total + product.price

        return total

    def show_all_products(self):
        print("\n--- All Products ---")

        for product in self.products:
            print(f"Product: {product.name} | Price: ${product.price:.2f}")

        print("--------------------")


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = input("Enter product price: ")

        new_product = Product(name, price)
        self.inventory.add_product(new_product)

    def show_summary(self):
        total_items = len(self.inventory.products)
        total_value = self.inventory.get_total_value()

        print(f"\n=== {self.store_name} Summary ===")
        print(f"Total Items in Inventory: {total_items}")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print("=======================\n")


# Testing the system

# 1. Create a Store object
my_store = Store("Tech Gadgets Outlet")

# 2. Add three products
print("Please enter details for 3 products:")

for i in range(3):
    my_store.add_new_product()

# 3. Display all products
my_store.inventory.show_all_products()

# 4. Display inventory summary
my_store.show_summary()

# 5. Combine the prices of the first two products
if len(my_store.inventory.products) >= 2:
    product1 = my_store.inventory.products[0]
    product2 = my_store.inventory.products[1]

    combined_price = product1 + product2

    print(
        f"Combined price of {product1.name} and {product2.name} "
        f"is: ${combined_price:.2f}"
    )
