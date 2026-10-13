def apply_discount(price, discount_percent=5):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


print(apply_discount(1000, 10))
print(apply_discount(500))