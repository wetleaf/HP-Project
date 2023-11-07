import re
import json


def read(path):
    with open(path, "r") as inp:
        match = inp.read()

    json_data = json.loads(match)
    data = json_data["Problem"]["Columns"]
    name = json_data["Name"]
    desc = json_data["Description"]
    ret_data = []
    for key in data.keys():
        col = [key]
        for i in range(len(data[key]["Entries"])):
            col.append(data[key]["Entries"][i])
        ret_data.append(col)
    sol_left = json_data["Solution"]["Left"]
    sol_right = json_data["Solution"]["Right"]
    return ret_data, name, desc, sol_left, sol_right
