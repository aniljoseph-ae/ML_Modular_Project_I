from pathlib import Path

project_structure = {
    "config": {
        "__init__.py": None,
        "config.yaml": None,
        "config.py": None,
        "schemas.py": None
        
    },
    "data": None,
    "notebooks": {
        "eda.ipynb": None,
        "test.ipynb": None
    },
    
    "src" : {
        "__init__.py": None,
        "data_loader.py": None,
        "preprocessing.py": None,
        "pipeline.py": None,
        "trainer.py": None,
        "tuner.py": None,
        "model.py": None,
        "logging_tracking.py": None,
    },
    "train": {
        "__init__.py": None,
        "tuning.py": None,
        "training.py": None,
        "evaluating.py": None,
    },
    "models":  None,
    "utils": {
        "__init__.py":None,
        "project_structure.py": None,
        "evaluation_metrics.py": None,
        "model_utils.py": None
    },
    "app.py": None,
    "README.md": None,
    "requirements.txt": None
}


def create_structure(base_path: Path, structure: dict):
    for name, content in structure.items():
        path = base_path / name
        
        if content is None:
            path.parent.mkdir(parents=True, exist_ok= True)
            path.touch(exist_ok = True)
            print(f"Created file: {path}")
            
        else:
            path.mkdir(parents=True, exist_ok = True)
            print(f"Create directory: {path}")
            create_structure(path, content)


if __name__ == "__main__":
    CWD = Path(__file__).resolve().parent
    ROOT_DIR = CWD.parent
    
    print(f"Creating project structure in : {ROOT_DIR}")
    create_structure(ROOT_DIR, project_structure)