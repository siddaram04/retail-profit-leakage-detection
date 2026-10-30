# Retail Profit Leakage Detection System

## Project Overview

The Retail Profit Leakage Detection System is a data analytics project designed to identify products, categories, and discount levels associated with retail profit losses.

The project uses Python for data cleaning and analysis and Microsoft Power BI for interactive visualization. It helps uncover areas where sales activity may not translate into healthy profitability and provides data-driven recommendations for improving pricing and discount decisions.

## Business Problem

Retail businesses can generate substantial sales while experiencing low profits or losses on particular products and transactions.

Excessive discounts, product-level losses, and differences in category profitability can make it difficult to understand where profit is being lost.

This project analyzes retail sales and profit data to identify potential profit leakage and support better business decisions.

## Objectives

- Analyze sales, profit, and profit margins across product categories.
- Identify discount levels associated with negative profits.
- Detect category and discount combinations with significant losses.
- Identify the most loss-making products.
- Build an interactive Power BI dashboard.
- Provide actionable recommendations based on the analysis.

## Tools and Technologies

- **Python** — Data processing and analysis
- **Pandas** — Data cleaning, grouping, aggregation, and analysis
- **NumPy** — Numerical operations
- **Microsoft Power BI** — Interactive dashboard and visualization
- **CSV** — Storage and transfer of processed analytical datasets
- **GitHub** — Project version control and portfolio presentation

## Project Workflow

1. **Data Preparation:** Load the retail dataset and inspect its structure.
2. **Data Analysis:** Analyze sales, profit, discount levels, categories, and products using Python.
3. **Profitability Analysis:** Identify negative-profit records and aggregate losses by relevant business dimensions.
4. **Data Export:** Export analytical results into CSV files.
5. **Dashboard Development:** Import the processed datasets into Power BI and build KPI cards, charts, and slicers.
6. **Business Recommendations:** Translate analytical findings into potential actions for improving profitability.

## Key Performance Indicators

The dashboard includes the following KPIs:

| KPI | Result |
|---|---:|
| Total Sales | 2.33M |
| Total Profit | 292.30K |
| Profit Margin | 12.56% |

These values represent the results of the current dataset analysis. The profit margin is calculated as total profit divided by total sales, multiplied by 100.

## Key Findings

### 1. Category Profitability

Furniture has a profit margin of approximately **2.61%**, compared with **17.22%** for Office Supplies and **17.45%** for Technology.

This indicates that Furniture has the weakest aggregate profit margin among the three categories analyzed.

**Recommendation:** Investigate product costs, pricing, and discount practices within the Furniture category.

### 2. Discount-Level Losses

The 70% discount group recorded an aggregate loss of approximately **40,301** in the dataset's currency.

The 80% discount group recorded an aggregate loss of approximately **30,565**.

These results identify high-discount transactions as an area for further investigation. They do not, by themselves, prove that discounts caused the losses.

**Recommendation:** Review heavily discounted transactions and evaluate whether the resulting profit justifies the discount offered.

### 3. Category and Discount Combinations

Office Supplies transactions with an 80% discount recorded an aggregate loss of approximately **30,565**.

Technology transactions with a 70% discount recorded an aggregate loss of approximately **19,579**.

**Recommendation:** Investigate these category-discount combinations to understand the contribution of product costs, selling prices, and discounting practices to negative profitability.

### 4. Loss-Making Products

The Cubify CubeX 3D Printer Double Head Print recorded a loss of approximately **8,880**, making it the largest loss-making product in the product analysis.

**Recommendation:** Examine its cost structure, pricing, discount history, and sales conditions before deciding whether to revise its pricing or sales strategy.

## Power BI Dashboard

The interactive dashboard contains:

- Total Sales KPI
- Total Profit KPI
- Profit Margin KPI
- Total Profit by Category
- Total Profit by Discount Level
- Top 10 Loss-Making Products
- Loss-Making Category and Discount Combinations
- Interactive category and discount slicers

The dashboard allows users to explore profitability patterns and investigate potential sources of profit leakage.

## Project Structure

```text
Retail-Profit-Leakage-Detection/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── category_analysis.csv
│       ├── discount_analysis.csv
│       ├── category_discount_analysis.csv
│       └── product_analysis.csv
│
├── main.py
├── requirements.txt
├── README.md
└── powerbi/
    └── Retail_Profit_Leakage.pbix
```

*Note: Adjust the folder and file names above to match your actual project structure.*

## How to Run the Project

### Prerequisites

- Python installed on your computer
- Visual Studio Code or another Python editor
- Required Python libraries
- Microsoft Power BI Desktop to open the dashboard

### Installation

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Ensure the raw dataset is located at the path expected by `main.py`.
5. Run the Python analysis:

```bash
python main.py
```

6. Open the Power BI `.pbix` file to explore the dashboard.

## Business Recommendations

Based on the analysis, the following actions warrant further investigation:

- Review pricing and costs for low-margin product categories.
- Evaluate the profitability of heavily discounted transactions.
- Investigate category-discount combinations with large aggregate losses.
- Examine individual loss-making products before changing their pricing or assortment.
- Monitor profit margin alongside sales to avoid focusing on revenue alone.

These recommendations should be validated against product costs, transaction details, and the retailer's broader business objectives before implementation.

## Conclusion

The Retail Profit Leakage Detection System demonstrates how Python and Power BI can be combined to analyze retail profitability, identify loss-making areas, and communicate findings through an interactive dashboard.

The project provides a foundation for data-driven decisions related to pricing, discount policies, product performance, and profit improvement.

## Author

**Siddaram Kotali**

MBA Student | Aspiring Data Analyst

Skills demonstrated: Python, Pandas, Data Analysis, Power BI, KPI Reporting, Data Visualization, and Business Insights.