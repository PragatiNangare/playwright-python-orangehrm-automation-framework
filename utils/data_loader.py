import json
def load_test_data():
    with open("data/test_data.json") as file:
        return json.load(file)
    