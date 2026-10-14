
import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

total_sales = np.sum(sales)
average_sales = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
std_deviation = np.std(sales)

print("Total Weekly Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Standard Deviation:", std_deviation)

above_average = sales[sales > average_sales]

print("Sales Above Average:", above_average)

# Identify the days with above-average sales
days = np.arange(1, 8)
above_average_days = days[sales > average_sales]

print("Days with Above-Average Sales:", above_average_days)
