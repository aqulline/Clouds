import json

from tabulate import tabulate

with open("data.json", "r") as f:
    data = json.load(f)
dt = tabulate(data, headers=("Issue Id", "Author", "Description"), tablefmt="pretty")

print(dt)