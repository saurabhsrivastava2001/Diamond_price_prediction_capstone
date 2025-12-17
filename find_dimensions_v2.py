import pandas as pd

try:
    df = pd.read_csv('notebooks/data/train.csv')
    
    # Filter for the specific diamond
    filtered_df = df[
        (df['carat'] >= 0.99) & (df['carat'] <= 1.01) &
        (df['cut'] == 'Ideal') &
        (df['color'] == 'G') &
        (df['clarity'] == 'VS1')
    ]
    
    with open('dimensions.txt', 'w') as f:
        if not filtered_df.empty:
            mean_vals = filtered_df[['depth', 'table', 'x', 'y', 'z']].mean()
            f.write("Found matches:\n")
            f.write(f"depth: {mean_vals['depth']:.2f}\n")
            f.write(f"table: {mean_vals['table']:.2f}\n")
            f.write(f"x: {mean_vals['x']:.2f}\n")
            f.write(f"y: {mean_vals['y']:.2f}\n")
            f.write(f"z: {mean_vals['z']:.2f}\n")
        else:
            f.write("No exact matches found.\n")
            
except Exception as e:
    with open('dimensions.txt', 'w') as f:
        f.write(f"Error: {e}")
