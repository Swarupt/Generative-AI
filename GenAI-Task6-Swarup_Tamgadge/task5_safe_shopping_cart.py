cart = []

while True:

    price = input("Enter price or q to quit: ")

    if price == "q":
        break

    try:
        price = float(price)

        if price < 0:
            raise ValueError("Negative price not allowed")

        cart.append(price)

        print("Price added successfully.")

    except ValueError as error:
        print(error)

print("\nTotal Items:", len(cart))

total_bill = 0

for price in cart:
    total_bill = total_bill + price

print("Total Bill:", total_bill)