def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount


def flat_discount(price):
    return price - 50