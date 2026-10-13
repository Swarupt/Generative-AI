prices = [100, 250, 400, 1200, 50, 2000, 850]

expensive_prices = list(filter(lambda price: price > 500, prices))

cheap_prices = list(filter(lambda price: price <= 500, prices))

print("Prices greater than 500:", expensive_prices)
print("Prices less than or equal to 500:", cheap_prices)