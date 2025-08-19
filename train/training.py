# ./train/training.py

from src.data_loader import load_data
from src.pipeline import create_pipeline
fom config.config import load_config, get_path
from utils.model_utils import save_model


def train_model():
    _ = load_config() # ensure config loads without error
    X_train, X_test, y_train, y_test = load_data()
    
    model = create_pipeline()
    model.fit(X_train, y_train)
    
    # save model
    model_path = get_path('model_dir') / "model.pkl"
    save_model(model, model_path)

    # evaluate model
    evaluate_model(model, X_test, y_test)
    

train_model()