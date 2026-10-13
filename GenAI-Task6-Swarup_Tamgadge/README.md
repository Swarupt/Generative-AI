# Assignment 6: Python - Exception Handling

## Overview

This assignment focuses on handling unexpected user inputs, invalid operations, and runtime errors using Python's exception handling system.

The programs demonstrate how to use try, except, else, finally, raise, and common built-in exceptions.

## Topics Covered

- try
- except
- Multiple except blocks
- else
- finally
- raise
- ValueError
- ZeroDivisionError
- TypeError
- FileNotFoundError
- PermissionError
- Basic input validation

## Tasks

### Task 1 - Safe Division Utility

Created a program that takes a numerator and denominator from the user and performs division.

The program handles:

- ValueError for invalid numeric input.
- ZeroDivisionError when the denominator is zero.

The `else` block displays the result when there is no error, and the `finally` block displays "Operation Complete".

### Task 2 - Bill Calculator with Error Handling

Processes a list of product prices and calculates the total of valid positive prices.

The program handles:

- TypeError for non-numeric values.
- ValueError for negative prices.

Invalid values are skipped and the program continues processing the remaining prices.

### Task 3 - Custom Exception: Age Validator

Created a `check_age()` function that validates whether an age is between 1 and 120.

A `ValueError` is raised with the message:

"Age must be between 1 and 120"

The error is caught using a try-except block.

### Task 4 - File Reader with Exception Handling

Created a program that asks the user for a filename and attempts to read the file.

The program handles:

- FileNotFoundError
- PermissionError

If the file is successfully opened, the first three lines are displayed.

A finally block displays "File operation attempted."

### Task 5 - Mini Program: Safe Shopping Cart

Created a simple shopping cart program that:

- Starts with an empty cart.
- Accepts prices from the user.
- Stops when the user enters `q`.
- Converts prices to float.
- Handles invalid input.
- Rejects negative prices.
- Calculates total items.
- Calculates the total bill.

## Files Included

- `task1_safe_division.py`
- `task2_bill_calculator.py`
- `task3_age_validator.py`
- `task4_file_reader.py`
- `task5_safe_shopping_cart.py`
- `README.md`

## Restrictions Followed

- No classes
- No modules
- No OOP
- No external packages
- Exception handling is the main focus
- Programs are kept simple and readable

## Objective

The objective of this assignment is to understand how Python handles runtime errors and invalid inputs using exception handling.

The assignment demonstrates the use of try, except, else, finally, raise, and different built-in exceptions.