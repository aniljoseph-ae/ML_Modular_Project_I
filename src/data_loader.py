# ./src/data_loader.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from config.config import load_config

def load_data():
    config = load_config()
    iris = load_iris(as_frame=True)
    X: pd.DataFrame = iris.data
    y = iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        random_state = config["data_loader"]['random_state'],
        test_size = config["data_loader"]["test_size"]
    )
    return X_train, X_test, y_train, y_test
    