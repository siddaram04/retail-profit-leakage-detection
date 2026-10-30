import pandas as pd
df = pd.read_excel("data/RAW/sample_superstore.xls")


# 1. Check the total number of rows
print("\n--- Profit Summary ---")
print("Total rows:", len(df))
print("Positive profit:", (df["Profit"] > 0).sum())
print("Zero profit:", (df["Profit"] == 0).sum())
print("Negative profit:", (df["Profit"] < 0).sum())

# 2. Analyze profitability by category
print("\n--- Category Profitability ---")

category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .reset_index()
)

category_analysis["Profit_Margin_Pct"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"]
    * 100
).round(2)

print(category_analysis.sort_values("Total_Profit").to_string(index=False))

# 3. Identify products that are losing money

print("\n--- Top 10 Loss-Making Products ---")

product_analysis = (
    df.groupby("Product Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)

loss_products = product_analysis[
    product_analysis["Total_Profit"] < 0
]

loss_products = loss_products.sort_values(
    "Total_Profit",
    ascending=True
).head(10)

print(loss_products.to_string(index=False))

#4 Analyze profitability by discount
print('\n--- Discount analysis')

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .reset_index()
)

print(discount_analysis.sort_values("Total_Profit").to_string(index=False))

# identify losses by category and discount
# 5. Identify losses by category and discount
print("\n--- Loss Analysis by Category and Discount ---")

category_discount_analysis = (
    df.groupby(["Category", "Discount"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .reset_index()
)

loss_combinations = category_discount_analysis[
    category_discount_analysis["Total_Profit"] < 0
]

loss_combinations = loss_combinations.sort_values(
    "Total_Profit",
    ascending=True
).head(15)

print(loss_combinations.to_string(index=False))

#6. investigate products with biggest discount-related losses
print("\n--- products: office supplies at 80% Discount ---")

high_discount_products = df[
    (df["Category"] == "Office Supplies") & (df["Discount"] == 0.8)
]
 
product_loss_analysis = (
    high_discount_products.groupby("Product Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)
product_loss_analysis = product_loss_analysis.sort_values(
        "Total_Profit", ascending=True
    )
print(product_loss_analysis.head(10).to_string(index=False))

#7. Export product loss analysis to csv
product_loss_analysis.to_csv("data/processed/product_loss_analysis.csv", index=False)
print("\nProduct loss analysis exported successfully")

#Export analysis result for power bi

category_analysis.to_csv("data/processed/category_analysis.csv", index=False)
discount_analysis.to_csv("data/processed/discount_analysis.csv", index=False)
category_discount_analysis.to_csv("data/processed/category_discount_analysis.csv", index=False)
product_analysis.to_csv("data/processed/product_analysis.csv", index=False)

print("\nAll analysis results exported successfully")