Sales Analysis Project

# 📊 Sales Analysis Project  

## 📌 Overview  
This project analyzes sales data to identify trends, top-performing products, regional sales, and profitability. We use Python for data processing and visualization, and Power BI for interactive dashboards.  

---

## 📂 Project Structure

📁 Sales-Analysis-Project
├── 📂 data          # Store raw and cleaned datasets
├── 📂 notebooks     # Python scripts for data processing
├── 📂 reports       # Charts, insights, Power BI files
├── README.md        # Project documentation

---

## 🛠️ Steps to Build the Project  

### **🔹 Step 1: Set Up the Project Structure**  
1️⃣ Create the project folder with the above structure.  
2️⃣ Store raw sales data inside the `data` folder.  

### **🔹 Step 2: Load and Clean Data**  
1️⃣ Create `load_data.py' 
2️⃣ Load the dataset using Pandas:  
   ```python
   import pandas as pd
   df = pd.read_csv("data/train.csv", parse_dates=["Order Date"])

3️⃣ Handle missing values:

df.dropna(inplace=True)  # Remove rows with missing data

4️⃣ Save the cleaned dataset:

df.to_csv("data/cleaned_sales_data_with_year_month.csv", index=False)

🔹 Step 3: Extract Date Information

1️⃣ Add Year and Month columns:

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

2️⃣ Verify missing values in Order Date:

missing_dates = df["Order Date"].isna().sum()
print(f"Missing Order Date values: {missing_dates}")

🔹 Step 4: Perform Sales Analysis

1️⃣ Aggregate monthly sales:

monthly_sales = df.groupby(["Year", "Month"])["Sales"].sum().reset_index()

2️⃣ Plot sales trends:

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_sales, x=monthly_sales.index, y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

3️⃣ Save the chart:

plt.savefig("reports/sales_month.png")

🔹 Step 5: Create Interactive Visuals in Power BI

1️⃣ Open Power BI Desktop.
2️⃣ Load final_sales_data.csv.
3️⃣ Create the following charts:

📈 Sales Trend Over Time (Line Chart) → X: month, Y: Sales

📊 Top-Selling Products (Bar Chart) → X: Product Name, Y: Total Sales

🌍 Regional Sales Analysis (Map or Bar Chart) → Fields: Region, Total Sales



4️⃣ Save the Power BI file in the reports/ folder as Sales_dashboard1.pbix.

🔹 Step 6: Save & Document the Project

1️⃣ Store all reports and charts in the reports/ folder.
2️⃣ Maintain a README.md with project details.
3️⃣ Share insights with stakeholders! 🚀


---

🔗 Results & Insights

📌 Monthly sales trends help identify peak business periods.
📌 Top-selling products guide inventory and marketing strategies.
📌 Regional analysis helps optimize supply chain and distribution.


---

💡 Future Improvements

🔹 Add customer segmentation analysis.
🔹 Use predictive analytics for future sales forecasting.
🔹 Automate data updates using Python scripts.


---

🛠️ Tech Stack

🔹 Python (Pandas, Matplotlib, Seaborn)
🔹 Power BI (Interactive Dashboards)
🔹 VS Code / PyCharm (Development)

