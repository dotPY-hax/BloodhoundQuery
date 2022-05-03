import json


def print_data(data):
    data = data if data else []
    for item in data:
        values = [str(value) for value in item.values()]
        print(" - ".join(values))


def print_json(data):
    try:
        data = json.loads(data)
    except TypeError:
        pass
    output_string = json.dumps(data, indent=4, sort_keys=True)
    print(output_string)
