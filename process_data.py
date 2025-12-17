import pandas as pd
import os

# Create data directory if not exists
os.makedirs('notebooks/data', exist_ok=True)

# URL for the new dataset
url = 'https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/diamonds.csv'

print(f"Reading data from {url}...")
df = pd.read_csv(url)

# The new dataset has columns: carat, cut, color, clarity, depth, table, price, x, y, z
# The old dataset had: id, carat, cut, color, clarity, depth, table, x, y, z, price

# Add 'id' column
df['id'] = df.index

# Reorder columns to match old schema
target_columns = ['id', 'carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z', 'price']

# check if all columns exist
for col in target_columns:
    if col not in df.columns:
        print(f"Warning: column {col} missing in new dataset")

df = df[target_columns]

output_path = 'notebooks/data/train.csv'
df.to_csv(output_path, index=False)
print(f"Saved processed data to {output_path}")
print(df.head())
