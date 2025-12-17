import urllib.request
import os

url = 'https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/diamonds.csv'
# Ensure directory exists
os.makedirs('notebooks/data', exist_ok=True)
print(f"Downloading from {url}...")
urllib.request.urlretrieve(url, 'notebooks/data/train.csv')
print("Download complete.")
