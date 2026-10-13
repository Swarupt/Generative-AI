# Assignment 3: Python - Functions

## Overview

This assignment focuses on Python functions and their different variations. 
The programs are based on simple billing and utility operations.

## Topics Covered

- User-defined functions
- Recursive functions
- Lambda functions
- map()
- filter()
- Default arguments
- Loops and function calls

## Tasks

### Task 1 - Basic Function: Price After Discount
Created a function `apply_discount()` to calculate the final price after applying a discount.

- Uses a default discount of 5%.
- Tests the function with different prices and discount percentages.

### Task 2 - Recursive Function: Factorial Utility
Created a recursive function `factorial()` to calculate the factorial of a number.

- Handles 0 and 1.
- Displays an error message for negative numbers.

### Task 3 - Lambda Function: GST Calculator
Created a lambda function `gst` to calculate the price after adding 18% GST.

### Task 4 - Using map(): Apply GST to List of Prices
Used `map()` with the GST lambda function to apply 18% GST to a list of prices.

### Task 5 - Using filter(): Filter Expensive Products
Used `filter()` to separate prices into two lists:

- Prices greater than 500
- Prices less than or equal to 500

### Task 6 - Combined Utility Function
Created a function `process_prices()` that:

- Applies a 10% discount using `map()`.
- Filters discounted prices greater than 300 using `filter()`.
- Returns both lists.

### Task 7 - Mini Problem: Menu Using Functions
Created a simple menu-driven program using functions.

The menu allows the user to:

1. Add a price
2. Show average price
3. Show highest price
4. Quit the program

## Files Included

- `task1_basic_function.py`
- `task2_recursive_function.py`
- `task3_lambda_gst.py`
- `task4_map_gst.py`
- `task5_filter_products.py`
- `task6_combined_utility.py`
- `task7_menu_functions.py`

## Restrictions Followed

- No classes
- No external packages
- No file handling
- No exception handling
- Simple and readable Python code
- Only concepts covered in the assignment are used

## Conclusion

This assignment demonstrates the use of Python functions, recursion, lambda functions, `map()`, `filter()`, default arguments, and loops through simple utility and billing-related programs.