import json

def open_json(path):
    with open(path, "r+") as outfile:
        json_prueba = json.load(outfile)
        return json_prueba 