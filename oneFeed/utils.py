import json
test_path  = './test.json'
def read_json_to_dict(json_path):
    with open(json_path) as f:
        a = json.load(f)
    return a
