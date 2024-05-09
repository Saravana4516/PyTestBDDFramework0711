import csv
import json
from os import path

def save_json(json_file_name, i, resp_body) :
    while path.exists(json_file_name):
        json_file_name = json_file_name[:json_file_name.rfind('_')] + '-' + str(i) + "json"
        i += 1
    print("Result saved at ", json_file_name)
    with open(json_file_name, 'w') as f:
        json.dump (resp_body, f)
    return json_file_name

