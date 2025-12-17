import pickle
import sys
import os

log_file = open("model_check.log", "w")

def log(msg):
    print(msg)
    log_file.write(msg + "\n")

log("Starting Model Check")

try:
    with open(os.path.join("artifacts", "preprocessor.pkl"), "rb") as f:
        log("Loading preprocessor...")
        preprocessor = pickle.load(f)
        log("Preprocessor loaded successfully.")
except Exception as e:
    log(f"ERROR loading preprocessor: {e}")

try:
    with open(os.path.join("artifacts", "model.pkl"), "rb") as f:
        log("Loading model...")
        model = pickle.load(f)
        log("Model loaded successfully.")
except Exception as e:
    log(f"ERROR loading model: {e}")

log("Model Check Complete")
log_file.close()
