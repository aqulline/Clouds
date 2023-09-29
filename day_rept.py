import json
import random


def write(data):
    with open("ble.json", "w") as file:
        initial_data = json.dumps(data, indent=4)
        file.write(initial_data)


def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data



data = load("ble.json")

repeat = []

prev_day = ""
prev_week = ""

for i, y in data.items():
    for k, j in y.items():
        if j["week"] == prev_week and j["day"] == prev_day:
            repeat.append(k)
            print(prev_day, prev_week)
            print(i, j["week"], j["day"])
        else:
            prev_day = j["day"]
            prev_week = j["week"]
    prev_week = ""
    prev_day = ""

print(len(repeat))

