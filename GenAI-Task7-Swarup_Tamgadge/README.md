# Assignment 7: Python — Object-Oriented Programming (OOP)

## Overview

This assignment focuses on the fundamental concepts of Object-Oriented Programming in Python. The programs demonstrate classes, objects, constructors, encapsulation, inheritance, polymorphism, abstraction, magic methods, operator overloading, and a simple inventory management system.

## Topics Covered

- Classes and Objects
- Constructors (`__init__`)
- Attributes and Methods
- Encapsulation and Private Attributes
- Getter and Setter Methods
- Single-Level Inheritance
- Method Overriding
- Polymorphism
- Abstraction and Abstract Base Classes
- Magic Methods
- Operator Overloading
- Inventory Management Using Classes

## Tasks

### Task 1 — Basic Class and Object Creation

Created a `Product` class with the attributes `name`, `price`, and `category`.

The `get_info()` method displays product details. Two product objects are created and tested. An optional `apply_discount()` method calculates the discounted price.

### Task 2 — Constructor and Encapsulation

Modified the `Product` class to use a private attribute `__price`.

Implemented:
- `get_price()` to retrieve the price.
- `set_price(new_price)` to update the price only when it is greater than zero.

### Task 3 — Inheritance

Created an `ElectronicProduct` class that inherits from `Product`.

Added the `warranty_years` attribute and overrode `get_info()` to display product details along with warranty information.

### Task 4 — Polymorphism

Created `Laptop` and `Mobile` classes that inherit from `Product`.

Both classes override `get_info()` to display product information in their own style. A loop calls the method on both objects to demonstrate polymorphism.

### Task 5 — Abstraction

Created an abstract base class `Payment` with the abstract method `process_payment(amount)`.

Implemented two subclasses:
- `CreditCardPayment`
- `UPIPayment`

Both subclasses override the abstract method to display their respective payment messages.

### Task 6 — Magic Methods and Operator Overloading

Added the following magic methods to the `Product` class:

- `__str__()` returns a readable string representation of a product.
- `__add__()` allows two product objects to be added using the `+` operator and returns their combined price.

### Task 7 — Mini Inventory Management System

Created a simple inventory management system using three classes:

**Product**
- Stores product name and price.
- Converts the product price to a floating-point number.
- Implements `__add__()` to return the combined price of two products.

**Inventory**
- Stores product objects in a list.
- Adds new products using `add_product()`.
- Removes products by name using `remove_product()`.
- Calculates the total inventory value using `get_total_value()`.
- Displays all products using `show_all_products()`.

**Store**
- Stores the store name and an `Inventory` object.
- Takes product details from the user through `add_new_product()`.
- Displays the total number of products and total inventory value using `show_summary()`.

The program accepts details for three products, displays an inventory summary, and demonstrates operator overloading by combining the prices of the first two products.

## Files Included

- `task1_product.py`
- `task2_encapsulation.py`
- `task3_inheritance.py`
- `task4_polymorphism.py`
- `task5_abstraction.py`
- `task6_operator_overloading.py`
- `task7_inventory_management.py`
- `README.md`

## Restrictions Followed

- Each task is implemented separately.
- Class structures are kept simple and readable.
- No file handling or external packages are used.
- The `abc` module is used for abstraction in Task 5.
- The programs focus on the required OOP concepts.

## How to Run

Open the `Assignment7` folder in VS Code or another Python editor.

Run each Python file separately to test the corresponding task. For Task 7, enter the names and prices of three products when prompted.

## Objective

The objective of this assignment is to understand the fundamental principles of Object-Oriented Programming and apply them to practical examples involving products, payments, and inventory management.