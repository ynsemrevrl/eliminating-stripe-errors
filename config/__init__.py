"""Config Initalizer"""
import yaml

with open("./config/config.yaml", "r", encoding="utf8") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError:
        print("Config file is not loaded.")

MODEL_CONFIG = config['model']

INFERENCE_CONFIG = config['inference']
