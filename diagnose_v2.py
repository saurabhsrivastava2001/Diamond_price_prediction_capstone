import sys
import os

with open('diagnostic_results.txt', 'w') as f:
    f.write("Diagnostic Start\n")
    try:
        import flask
        f.write(f"Flask installed: {flask.__version__}\n")
    except ImportError as e:
        f.write(f"Flask Import Error: {e}\n")

    try:
        import pandas as pd
        f.write(f"Pandas installed: {pd.__version__}\n")
        if os.path.exists('notebooks/data/train.csv'):
            try:
                df = pd.read_csv('notebooks/data/train.csv')
                f.write(f"Data Loaded. Shape: {df.shape}\n")
                f.write(f"Columns: {df.columns.tolist()}\n")
            except Exception as e:
                f.write(f"Data Read Error: {e}\n")
        else:
            f.write("Data file 'notebooks/data/train.csv' NOT FOUND\n")
    except ImportError as e:
        f.write(f"Pandas Import Error: {e}\n")
    except Exception as e:
        f.write(f"Data Error: {e}\n")

    f.write("Diagnostic End\n")
