prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:

    try:
        if not isinstance(price, (int, float)):
            raise TypeError

        if price < 0:
            raise ValueError("Negative price not allowed")

        if price > 0:
            total = total + price
            print("Running Total:", total)

    except TypeError:
        print("Invalid price: value is not a number.")

    except ValueError as error:
        print(error)

print("Final Total:", total)