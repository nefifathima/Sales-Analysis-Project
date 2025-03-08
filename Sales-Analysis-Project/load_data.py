# Import necessary libraries
import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")  # Ensure the correct file path

# Display basic info before cleaning
print("Before Cleaning:")
print(df.info())

# 🔹 Step 1: Remove Duplicates
df.drop_duplicates(inplace=True)

# 🔹 Step 2: Handle Missing Values
df.fillna(0, inplace=True)  # Replace missing values with 0 (modify as needed)

# 🔹 Step 3: Convert Date Column to Proper Format
df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')  # Convert to DateTime

# 🔹 Step 4: Remove Unnecessary Columns (if needed)
#df.drop(columns=["UnnecessaryColumn"], inplace=True)  # Uncomment if needed

# Display basic info after cleaning
print("\nAfter Cleaning:")
print(df.info())

# Save the cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)
print("\n Data Cleaning Complete! Cleaned file saved as 'cleaned_sales_data.csv'")
