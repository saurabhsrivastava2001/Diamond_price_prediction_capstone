import pandas as pd
try:
    df = pd.read_csv('notebooks/data/train.csv')
    min_price = df['price'].min()
    print(f"Minimum Price in Dataset: {min_price}")
except Exception as e:
    print(f"Error: {e}")
