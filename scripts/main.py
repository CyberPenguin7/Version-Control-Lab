import pandas as pd

df = pd.read_csv("../data/sales_data.csv")

assert (df["price"] >= 0).all(), "Found negative prices"