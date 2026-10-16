# Assignment 12: Seaborn (Relational, Distribution, Categorical & Multi-Plots)



## Dataset Information
- **Dataset File:** `sales_data (1).csv`
- **Features Used:**
  - **Numerical Columns:** `Sales_Amount`, `Quantity_Sold`, `Unit_Price`, `Unit_Cost`, `Discount`
  - **Categorical Columns:** `Product_Category`, `Region`, `Customer_Type`, `Payment_Method`, `Sales_Channel`

---

## Task Overview & Implementation Summary

### Task 1: Relational Plot (`sns.relplot`)
- Created a relational scatter plot showing the relationship between `Quantity_Sold` and `Sales_Amount`.
- Used `hue='Product_Category'` to distinguish categories visually.
- Applied custom markers and styles (`style='Product_Category'`).

### Task 2: Line Plot as Scatter & Facet (`sns.lineplot` & `FacetGrid`)
- Built a standard line plot using `sns.lineplot()`.
- Created a scatter-style line plot with explicit markers (`marker='o'`).
- Applied faceting (`sns.FacetGrid`) using `col='Region'` to separate line plots across different regions.

### Task 3: Distribution Plots (`sns.histplot`, `sns.kdeplot`, `sns.rugplot`)
- Plotted a univariate **Histogram** of `Sales_Amount`.
- Plotted a **Kernel Density Estimate (KDE)** plot.
- Plotted a **Rug plot** showing marginal data points.
- Combined **Histogram + KDE** into a single overlay plot (`kde=True`).

### Task 4: Bivariate Distribution Plots
- Created a **2D Bivariate Histogram** showing joint density between `Quantity_Sold` and `Sales_Amount`.
- Created a **2D Bivariate KDE Plot** to display density contours across numerical columns.

### Task 5: Matrix Plots (`sns.pairplot`, `sns.heatmap`)
- Generated a **Pair Plot** (`sns.pairplot`) across key numerical features (`Sales_Amount`, `Quantity_Sold`, `Unit_Price`, `Unit_Cost`).
- Computed the Pearson correlation matrix using Pandas and rendered a **Correlation Heatmap** with annotations (`annot=True`).

### Task 6: Categorical Plots
- **Bar Plot:** Displayed average `Sales_Amount` per `Product_Category`.
- **Box Plot:** Showed the 5-number summary and outliers across categories.
- **Violin Plot:** Combined box plot summary with kernel density estimation.
- **Count Plot:** Counted categorical occurrences across product categories.

### Task 7: Regression Plots (`sns.regplot`, `sns.lmplot`)
- Built a linear regression plot (`sns.regplot`) comparing `Quantity_Sold` vs `Sales_Amount`.
- Created an `sns.lmplot()` with `hue='Product_Category'` to compare regression lines per category.

### Task 8: Multi-Plots & Figure-Level Dashboards
- Constructed a custom **FacetGrid** mapping scatter plots across `Product_Category`.
- Designed multi-plot figure-level dashboards using:
  - `sns.relplot` (faceted scatter grid by region)
  - `sns.catplot` (faceted categorical bar grid)
  - `sns.displot` (faceted density distributions)

---
