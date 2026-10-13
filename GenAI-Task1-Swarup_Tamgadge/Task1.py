# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list of product names
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

print("Original Product List:")
print(products)


# 2. Create a tuple containing product name, price and category
sample_product = ("Laptop", 55000, "Electronics")

print("\nSample Product:")
print(sample_product)


# 3. Print the 2nd and last product
print("\nSecond Product:")
print(products[1])

print("Last Product:")
print(products[-1])


# 4. Add two new products
products.append("Printer")
products.append("Speaker")

print("\nUpdated Product List:")
print(products)


# Extra: Convert tuple into list, change price and convert it back
sample_product = list(sample_product)

sample_product[1] = 60000

sample_product = tuple(sample_product)

print("\nUpdated Sample Product:")
print(sample_product)