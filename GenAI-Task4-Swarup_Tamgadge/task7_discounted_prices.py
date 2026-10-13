prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percent = float(input("Enter discount percentage: "))


with open("discount_report.txt", "w") as file:

    file.write("Product | Original Price | Discounted Price\n")

    for product in prices:

        original_price = prices[product]

        discount = original_price * discount_percent / 100

        discounted_price = original_price - discount

        file.write(
            product + " | " +
            str(original_price) + " | " +
            str(discounted_price) + "\n"
        )


with open("discount_report.txt", "r") as file:

    content = file.read()

print("\nDiscount Report:")
print(content)
