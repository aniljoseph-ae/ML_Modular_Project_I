import sys
from pathlib import Path
import yaml

# get project root
CURRENT_DIR = Path(__file__).resolve()
ROOT_DIR = ROOT_DIR.parent[1]
CONFIG_DIR = ROOT_DIR / "config"

# Add root to system path
sys.path.append(str(ROOT_DIR))


# load configuration
def load_config():
    CONFIG_PATH = CONFIG_DIR / "config.yaml"
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
    return config

def get_path(name: str) -> Path:
    config = load_config()
    try:
        path = config['paths'][name]
    except KeyError as e:
        raise keyError(f"Path key {name} not found in config['paths]") from e
    return  ROOT_DIR / path