order_amount = int(input("Enter order amount: "))

if order_amount >= 2000:
    discount = order_amount * 15 / 100
elif order_amount >= 1500:
    discount = order_amount * 10 / 100
elif order_amount >= 1000:
    discount = order_amount * 7 / 100
else:
    discount = 0

final_amount = order_amount - discount

print("Order Amount:", order_amount)
print("Discount:", discount)
print("Final Amount:", final_amount)