# Task 2: Categories (Sets)

# Product list
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

# Category list corresponding to each product
categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Audio",
    "Electronics"
]


# 1. Create a set of categories
categories_set = set(categories)

print("Categories Set:")
print(categories_set)


# 2. Add a new category
categories_set.add("Gaming")

print("\nAfter Adding New Category:")
print(categories_set)

# Adding duplicate category
categories_set.add("Electronics")

print("\nAfter Adding Duplicate Category:")
print(categories_set)


# 3. Check whether a category exists
print("\nIs Electronics present?")
print("Electronics" in categories_set)

print("\nIs Clothing present?")
print("Clothing" in categories_set)


# Extra: Total number of unique categories
print("\nTotal Number of Unique Categories:")
print(len(categories_set))