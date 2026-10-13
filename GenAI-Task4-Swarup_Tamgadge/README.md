# Assignment 4: Python - File Handling

## Overview

This assignment focuses on file handling operations in Python. 
The programs demonstrate how to create, write, read, append, and process data stored in text files.

## Topics Covered

- Opening files in different modes
- Read mode (`r`)
- Write mode (`w`)
- Append mode (`a`)
- `read()`
- `readline()`
- `readlines()`
- `with open()`
- Writing data to text files
- Reading and processing file data
- Basic file existence checking

## Tasks

### Task 1 - Write Sales Records to a File

Creates a list of sales amounts and writes each sales value to `sales_data.txt` using write mode.

### Task 2 - Read File in Different Ways

Reads `sales_data.txt` using:

- `read()`
- `readline()`
- `readlines()`

The sales values are also converted from strings into integers.

### Task 3 - Append New Sales

Adds new sales values to the existing `sales_data.txt` file using append mode without removing the existing data.

### Task 4 - Generate Summary Report from File

Reads the sales data from the file and calculates:

- Total Sales
- Highest Sale
- Lowest Sale
- Average Sale

### Task 5 - Create Product Info File

Takes three product names and prices from the user and stores the information in `products.txt`.

### Task 6 - Read File Safely

Asks the user for a filename and checks whether the file exists before reading it.

### Task 7 - Extract Discounted Prices

Uses a dictionary of product prices, applies a user-provided discount percentage, and stores the original and discounted prices in `discount_report.txt`.

## Files Included

- `task1_write_sales.py`
- `task2_read_file.py`
- `task3_append_sales.py`
- `task4_summary_report.py`
- `task5_product_info.py`
- `task6_file_safety.py`
- `task7_discounted_prices.py`
- `README.md`

## Generated Files

The following text files are created when the programs are executed:

- `sales_data.txt`
- `products.txt`
- `discount_report.txt`

## Restrictions Followed

- No external libraries or packages except `os` where specifically allowed.
- No classes.
- No exception handling.
- No advanced concepts.
- Used `open()` for file operations.
- Programs are kept simple and readable.

## Execution Order

Tasks 1 to 4 should be executed in order because they use the same `sales_data.txt` file.

Task 5, Task 6, and Task 7 can be executed separately.

## Objective

The objective of this assignment is to understand basic Python file handling operations and learn how to store, read, update, and process data using text files.