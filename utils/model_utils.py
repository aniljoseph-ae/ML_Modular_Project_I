# ./utils/model_utils.py

from joblib
from pathlib import Path

def save_model(model, path: Path):
    path.parent.mkdir(parents = True, exist_ok = True)
    joblib.dump(model, path)
    print(f"Model saved at: {path}")
    
def load_model(path: Path):
    return joblib.load(path)