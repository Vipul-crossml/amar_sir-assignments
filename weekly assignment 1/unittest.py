import json
import unittest
json_string = None

with open("output.json") as f:
    json_string = f.read()
try:
    parsed_json = json.loads(json_string)
    formatted_json = json.dumps(parsed_json, indent = 6,sort_keys=True)
    with open("output.json", "w") as f:
        f.write(formatted_json)
except Exception as dis:
    print(repr(dis))
