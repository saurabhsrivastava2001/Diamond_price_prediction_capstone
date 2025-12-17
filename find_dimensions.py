import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('notebooks/data/train.csv')
    
    # Filter for the specific diamond
    filtered_df = df[
        (df['carat'] >= 0.99) & (df['carat'] <= 1.01) &
        (df['cut'] == 'Ideal') &
        (df['color'] == 'G') &
        (df['clarity'] == 'VS1')
    ]
    
    if not filtered_df.empty:
        print("Found matching diamonds in dataset:")
        print(filtered_df[['depth', 'table', 'x', 'y', 'z']].describe())
        print("\nRepresentative row (Mean):")
        print(filtered_df[['depth', 'table', 'x', 'y', 'z']].mean())
    else:
        print("No exact matches found. Broadening search...")
        # Broaden search if exact match fails
        filtered_df = df[
            (df['carat'] >= 0.95) & (df['carat'] <= 1.05) &
            (df['cut'] == 'Ideal')
        ]
        print(filtered_df[['depth', 'table', 'x', 'y', 'z']].mean())
        
except Exception as e:
    print(f"Error: {e}")
