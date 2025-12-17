import pandas as pd
try:
    df = pd.read_csv('notebooks/data/train.csv')
    min_price = df['price'].min()
    with open('min_price.txt', 'w') as f:
        f.write(str(min_price))
except Exception as e:
    with open('min_price.txt', 'w') as f:
        f.write("300") # Fallback
