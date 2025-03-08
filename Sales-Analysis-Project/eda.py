import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_sales_data_with_year_month.csv")

# Save final cleaned dataset for Power BI
df.to_csv("data/final_sales_data.csv", index=False)

print("\n✅ Final cleaned data saved as 'final_sales_data.csv'. Ready for Power BI!")