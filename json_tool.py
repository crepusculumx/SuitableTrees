import json


def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def write_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        # f.write(json.dumps(data, indent=2, ensure_ascii=False))
        f.write(json.dumps(data, ensure_ascii=False))
