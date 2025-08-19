# ./src/pipeline.py

from src.preprocessing import data_preprocessing_pipeline
from config.config import load_config

from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

def create_pipeline():
    config = load_config()
    
    model_params = config["model"]["params"]
    
    pipeline = Pipeline(
        steps = [
            ("preprocess", data_preprocessing_pipeline),
            {"classifier", XGBClassifier(**model_params)}
        ]
    )
    return pipeline