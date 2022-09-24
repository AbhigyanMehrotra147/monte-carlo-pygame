import json

with open('assets/boy-run/boy_run.json') as file:
    json_object = json.load(file)
    x = (json.dumps(json_object, indent = 3))
    boy_run_data = x
    print(x)
