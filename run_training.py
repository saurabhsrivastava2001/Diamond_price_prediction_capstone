import sys
import os

# Add src to python path
src_path = os.path.join(os.getcwd(), 'src')
sys.path.append(src_path)

from DimondPricePrediction.pipelines.training_pipeline import *

print("Training Pipeline Executed Successfully")
