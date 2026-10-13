def calculate_total(prices):
    total = 0

    for price in prices:
        total = total + price

    return total


def apply_tax(amount):
    return amount * 1.05