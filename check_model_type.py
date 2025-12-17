import pickle
import os
import sys

try:
    with open(os.path.join("artifacts", "model.pkl"), "rb") as f:
        model = pickle.load(f)
        print(f"Loaded Model Type: {type(model).__name__}")
        if hasattr(model, 'coef_'):
            print(f"Coefficients: {model.coef_}")
        if hasattr(model, 'intercept_'):
            print(f"Intercept: {model.intercept_}")
except Exception as e:
    print(f"Error loading model: {e}")
