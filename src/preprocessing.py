# ./src/preprocessing.py

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

numerical_features = make_column_selector(dtype_include = 'number')
categorical_features = make_column_selector(dtype_include = 'object')

# Numerical preprocessing
numerical_preprocessing = Pipeline(
    steps = [
        ("imputer", SimpleImputer(strategy = 'median')),
        ("scaler", StandardScaler())
    ]
)

#  Categorical preprocessing

categorical_preprocessing = Pipeline(
    steps = [
        ("imputer", SimpleImputer(strategy = 'most_frequent')),
        ("onehot", OneHotEncoder(handle_unknown = 'ignore'))
    ]
)

# column-wise preprocessing

data_preprocessing_pipeline = ColumnTransformer(
    transformers = [
        ("numerical preprocessing", numerical_preprocessing, numerical_features),
        ("categorical preprocessing", categorical_preprocessing, categorical_features)
    ],
    remainder = 'passthrough'
)
