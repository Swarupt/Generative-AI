orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order Amount\tDiscount\tFinal Amount")

for order_amount in orders:

    if order_amount >= 2000:
        discount = order_amount * 15 / 100
    elif order_amount >= 1500:
        discount = order_amount * 10 / 100
    elif order_amount >= 1000:
        discount = order_amount * 7 / 100
    else:
        discount = 0

    final_amount = order_amount - discount

    print(order_amount, "\t\t", discount, "\t\t", final_amount)

    total_revenue = total_revenue + final_amount

    if discount > 0:
        discounted_orders = discounted_orders + 1

print("Total Revenue:", total_revenue)
print("Number of Discounted Orders:", discounted_orders)