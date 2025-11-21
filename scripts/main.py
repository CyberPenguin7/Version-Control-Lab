import pandas as pd
df = pd.read_csv("../data/sales_data.csv")
assert (df["price"] >= 0).all(), "Found negative prices"

#Accuracy
print("Accuracy Check")
df["date"] = pd.to_datetime(df["date"])
negative_prices = (df["price"] < 0).sum()
print(f"Negative prices: {negative_prices}")


current_date = pd.Timestamp.now()
future_dates = (df["date"] > current_date).sum()
print(f"Future dates: {future_dates}")

#Consistency
print("Consistency Check")
unique_products = df["product"].unique()
unique_products_count = df["product"].nunique()
print("Unique products:", unique_products)
print("Count of unique products:", unique_products_count)

#Completeness
print("Completeness Check")
missing_values = df.isnull().sum()
print("Missing Values:", missing_values)
completeness_rate = df.notnull().mean().mean() * 100
print(f"Overall completeness rate: {completeness_rate:.1f}%")