# Sales Analysis Project  

## Overview  
This project analyzes sales data to identify trends, top-performing products, regional sales. We use Python for data processing and visualization, and Power BI for interactive dashboards.  

## Project Structure

Sales-Analysis-Project
- data          # Store raw and cleaned datasets
- notebooks     # Python scripts for data processing
- reports       # Charts, insights, Power BI files
- README.md        # Project documentation

##  Steps to Build the Project  

Step 1: Set Up the Project Structure 
1️. Create the project folder with the above structure.  
2️. Store raw sales data inside the `data` folder.  

Step 2: Load and Clean Data
1️. Create `load_data.py' 
2️. Load the dataset using Pandas  

Step 3️: Handle missing values
Step 4️: Save the cleaned dataset
Step 5: Extract Date Information
1. Add Year and Month columns
2. Verify missing values in Order Date

Step 6: Perform Sales Analysis
1. Aggregate monthly sales
2. Plot sales trends
3. Save the chart

Step 7: Create Interactive Visuals in Power BI
1️. Open Power BI Desktop.
2️. Load final_sales_data.csv.
3️. Create the following charts:

*Sales Trend Over Time (Line Chart) → X: month, Y: Sales

* Top-Selling Products (Bar Chart) → X: Product Name, Y: Total Sales

* Regional Sales Analysis (Map or Bar Chart) → Fields: Region, Total Sales



step 8: Save the Power BI file in the reports/ folder as Sales_dashboard1.pbix.

Step 9: Save & Document the Project


 ## Results & Insights

1. Monthly sales trends help identify peak business periods.
2. Top-selling products guide inventory and marketing strategies.
3. Regional analysis helps optimize supply chain and distribution.

 ## Future Improvements

1. Add customer segmentation analysis.
2. Use predictive analytics for future sales forecasting.
3. Automate data updates using Python scripts.

 ## Tech Stack

1. Python (Pandas, Matplotlib, Seaborn)
2. Power BI (Interactive Dashboards)
3. VS Code / PyCharm (Development)

