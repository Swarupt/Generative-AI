# Task 3: Product Pricing (Dictionaries)

# 1. Create a dictionary of products and prices
price_dict = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500,
    "Webcam": 3000
}

print("Original Price Dictionary:")
print(price_dict)


# 2. Update the price of an existing product
product = "Mouse"

if product in price_dict:
    price_dict[product] = 1000
    print("\nUpdated Mouse Price:")
    print(price_dict)
else:
    print("\nProduct does not exist")


# 3. Add a new product
product = "Printer"
price = 8000

if product in price_dict:
    price_dict[product] = price
else:
    price_dict[product] = price

print("\nAfter Adding New Product:")
print(price_dict)


# Handle a product that does not exist
product = "Tablet"

if product in price_dict:
    price_dict[product] = 15000
else:
    print("\nTablet does not exist in the dictionary")


# 4. Calculate average price
total = sum(price_dict.values())
average = total / len(price_dict)

print("\nAverage Price:")
print(average)


# Extra: Maximum and minimum price
maximum_price = max(price_dict.values())
minimum_price = min(price_dict.values())

print("\nMaximum Price:")
print(maximum_price)

print("Minimum Price:")
print(minimum_price)