with open("products.txt", "w") as file:

    for i in range(3):

        product_name = input("Enter product name: ")
        price = input("Enter product price: ")

        file.write(product_name + " | " + price + "\n")


with open("products.txt", "r") as file:

    content = file.read()

print("\nProduct Information:")
print(content)