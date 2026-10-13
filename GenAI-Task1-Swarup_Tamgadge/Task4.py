# Task 4: Combined Operations

# Product list
products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones",
    "Webcam"
]


# Price dictionary
price_dict = {
    "Laptop": 55000,
    "Mouse": 1000,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500,
    "Webcam": 3000
}


# Category list
categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Audio",
    "Electronics"
]


# 1. Create catalog as a list of tuples
catalog = []

for i in range(len(products)):
    product_name = products[i]
    price = price_dict[product_name]
    category = categories[i]

    catalog.append((product_name, price, category))


print("Catalog:")
print(catalog)


# 2. Create category_to_products dictionary
category_to_products = {}

for product in catalog:

    product_name = product[0]
    category = product[2]

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product_name)


print("\nCategory to Products:")
print(category_to_products)


# 3. Find the category with maximum number of products
maximum_category = ""

maximum_count = 0

for category in category_to_products:

    count = len(category_to_products[category])

    if count > maximum_count:
        maximum_count = count
        maximum_category = category


print("\nCategory with Maximum Number of Products:")
print(maximum_category)

print("\nProducts in this Category:")

for product in category_to_products[maximum_category]:
    print(product)