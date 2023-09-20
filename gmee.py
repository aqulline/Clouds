import string
import random
import json

randmed = []


def randomz():
    num1, num2 = random.choice(num), random.choice(num)
    data = f"{num1}{num2}"

    if data in randmed:
        randomz()
    else:
        randmed.append(data)

        return data


def load(data_file_name):
    with open(data_file_name, "r") as file:
        initial_data = json.load(file)
    return initial_data


def write(data):
    loaded = load("code.json")
    with open("code.json", "w") as file:
        final = {**loaded, **data}
        final_data = json.dumps(final, indent=4)
        file.write(final_data)


letter = string.ascii_lowercase

num = string.digits

for i in letter:
    data = {i: randomz()}

    write(data)
