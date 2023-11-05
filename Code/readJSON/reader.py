import re
import json


def read(path):
    with open(path, "r") as inp:
        file_contents = inp.read()

    pattern = r"<JSON>\n(.*)\n</JSON>"
    matches = re.findall(pattern, file_contents, re.DOTALL)

    match = matches[0]
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

    return ret_data, name, desc
