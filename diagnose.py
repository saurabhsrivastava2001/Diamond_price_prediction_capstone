import sys
import os

print("Diagnostic Start")
try:
    import flask
    print(f"Flask installed: {flask.__version__}")
except ImportError as e:
    print(f"Flask Import Error: {e}")

try:
    import pandas as pd
    print(f"Pandas installed: {pd.__version__}")
    if os.path.exists('notebooks/data/train.csv'):
        df = pd.read_csv('notebooks/data/train.csv')
        print(f"Data Loaded. Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
    else:
        print("Data file 'notebooks/data/train.csv' NOT FOUND")
except ImportError as e:
    print(f"Pandas Import Error: {e}")
except Exception as e:
    print(f"Data Error: {e}")

print("Diagnostic End")
