# Assignment 10: Pandas — Series, DataFrames, Functions, Filtering & Analysis

## Overview

This assignment focuses on using Pandas to organize, manipulate, filter, and analyze student marks and sales data. It covers Series, DataFrames, mathematical operations, statistical functions, grouping, and simple plotting.

## Topics Covered

- Pandas Series
- Series indexing and data types
- Mathematical operations on Series
- Lambda functions and basic Python functionalities
- Creating DataFrames
- DataFrame shape, columns, and information
- `head()`, `tail()`, `describe()`, and `info()`
- Sorting and resetting the index
- Filtering and conditional selection
- Grouping and aggregation using `groupby()`
- Bar graphs, line graphs, and histograms
- Sales data analysis

## Tasks

### Task 1 — Pandas Series Basics

Created a Series from student marks and displayed its values, index, and data type. Accessed the first element and the last two elements.

### Task 2 — Mathematical Operations on Series

Performed addition, subtraction, multiplication, and division on all student marks using vectorized Series operations.

### Task 3 — Python Functionalities on Series

Calculated maximum, minimum, sum, and mean marks. Used a lambda function to identify passing students and counted the number of students who passed.

### Task 4 — Create a DataFrame

Created a DataFrame containing student names, marks, and subjects. Displayed the first three rows, last two rows, shape, and column names.

### Task 5 — Important DataFrame Functions

Used `info()`, `describe()`, `head()`, and `tail()`. Sorted students by marks in descending order and reset the index.

### Task 6 — Filtering and Conditional Selection

Filtered students who scored more than 75 marks, students studying Mathematics, students scoring above average, and students who failed.

### Task 7 — Grouping and Basic Analysis

Used `groupby()` to calculate average marks, student counts, and maximum marks for each subject.

### Task 8 — Pandas Plotting

Created a bar graph of student marks, a line graph of marks, and a histogram using Pandas built-in plotting methods.

### Task 9 — Sales Data Analysis

Calculated total revenue, average daily revenue, the day with the highest revenue, and days with above-average revenue. Created a line graph of daily revenue.

## Files Included

- `assignment10_pandas.py`
- `README.md`

## Requirements

- Python
- Pandas
- Matplotlib for displaying Pandas-generated plots

## Installation

Install the required libraries using:

`pip install pandas matplotlib`

## How to Run

1. Open the `pandas_assignment` folder in VS Code.
2. Open the terminal in that folder.
3. Run the program using:

   `python assignment10_pandas.py`

4. The program prints the analysis results and displays the graphs.

## Restrictions Followed

- Pandas is used for Series, DataFrames, filtering, grouping, and analysis.
- No machine learning or advanced exploratory data analysis is included.
- Vectorized operations are used instead of unnecessary loops.
- Graphs are simple and created using Pandas built-in plotting.
- All nine tasks are arranged in the required order in one Python file.

## Objective

The objective is to learn how to work with tabular data using Pandas and perform basic numerical analysis, filtering, grouping, and visualization.