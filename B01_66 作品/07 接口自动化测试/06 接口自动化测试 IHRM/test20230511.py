import app
import json


def build_data2():
    json_file = app.BASE_DIR + r"\data\login.json"
    with open(json_file, encoding = 'utf-8') as f:
        login_data = json.load(f)
        for cd in login_data:
            desc = cd['desc']

    return login_data

print(build_data2())

