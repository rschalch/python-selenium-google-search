import json


def read(file):
    with open(file, 'r') as f:
        return f.read()


def write(file, output):
    with open(file, 'w+', encoding='utf8') as f:
        f.write(output)


def make_obj(json_str, first_key=False):
    if first_key:
        return list(json.loads(json_str).values())[0]
    return json.loads(json_str)


def make_json(obj, key=None):
    if key:
        result = {key: obj[key]}
        return json.dumps(result, ensure_ascii=False, indent=4)
    return json.dumps(obj, ensure_ascii=False, indent=4)
