import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_sales_data_with_year_month.csv")

# Group by City and sum sales
city_sales = df.groupby("City")["Sales"].sum().nlargest(10)

# Plot
plt.figure(figsize=(10,5))
city_sales.plot(kind="bar", color="orange")
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)


plt.savefig("reports/sales_region.png")
print("chart saved in reports/")
plt.show()