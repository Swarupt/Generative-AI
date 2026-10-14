# Assignment 8: Streamlit — Basic App Building

## Overview

This assignment focuses on creating simple and interactive web applications using Streamlit in Python. The applications demonstrate user input, buttons, selection components, calculations, and basic visual displays.

## Topics Covered

- Creating Streamlit applications
- `st.title()`
- `st.write()`
- `st.text_input()`
- `st.number_input()`
- `st.slider()`
- `st.button()`
- `st.selectbox()`
- Streamlit sidebar
- `st.success()` and `st.error()`
- `st.table()`
- `st.metric()`
- `st.bar_chart()`

## Tasks

### Task 1 — Basic Streamlit App

Created `app_basic.py` to display a welcome message, accept the user's name, and display a personalized greeting when the user clicks the "Greet Me" button.

### Task 2 — Price Calculator

Created `app_discount.py` to accept a product price and discount percentage. It calculates the discounted price and displays the result using `st.success()` and a simple table.

### Task 3 — Product Form

Created `app_product_form.py` with a sidebar form that accepts the product name, category, and price. It displays a success message and the product details after the user clicks "Add Product".

### Task 4 — Mini Sales Dashboard

Created `app_dashboard.py` to display a simple sales dashboard. It allows the user to select a month, displays the selected month's sales, and shows a bar chart of monthly sales.

## Files Included

- `app_basic.py`
- `app_discount.py`
- `app_product_form.py`
- `app_dashboard.py`
- `README.md`

## Restrictions Followed

- No authentication, APIs, databases, or file uploads.
- No pandas or external data-processing libraries.
- Simple Python calculations and lists are used.
- Streamlit components are used to build the user interface.
- Each task is implemented in a separate Python file.

## How to Run

1. Install Streamlit using `pip install streamlit`.
2. Open the assignment folder in VS Code.
3. Open the terminal in that folder.
4. Run the required application using:

   `streamlit run app_basic.py`

5. Replace `app_basic.py` with `app_discount.py`, `app_product_form.py`, or `app_dashboard.py` to run another task.

## Objective

The objective of this assignment is to understand the basics of Streamlit and learn how to build simple interactive applications using user inputs, buttons, calculations, tables, metrics, and charts.