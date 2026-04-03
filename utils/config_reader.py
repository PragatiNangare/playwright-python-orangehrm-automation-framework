import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        data = yaml.safe_load(file)
        return data
    