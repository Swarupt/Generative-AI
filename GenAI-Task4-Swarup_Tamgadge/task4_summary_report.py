with open("sales_data.txt", "r") as file:

    lines = file.readlines()


sales = []

for line in lines:
    sales.append(int(line.strip()))


total_sales = 0

for sale in sales:
    total_sales = total_sales + sale


highest_sale = sales[0]

for sale in sales:

    if sale > highest_sale:
        highest_sale = sale


lowest_sale = sales[0]

for sale in sales:

    if sale < lowest_sale:
        lowest_sale = sale


average_sale = total_sales / len(sales)


print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)