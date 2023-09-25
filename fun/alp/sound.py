import json


def load():
    with open("/home/alpha/PycharmProjects/Clouds/time.json", "r") as file:
        initial_data = json.load(file)
    return initial_data


data = load()

keys = data.keys()

days = {}

for u in keys:
    datas = data[u]
    dayy = datas.values()
    i = [i for i in dayy]
    day = i[0]["day"]
    timin = i[0]["time_in"]
    vnue = i[0]["venue"]

    if day not in days:
        days[day] = {}

    days[day][timin] = {
        "venue": vnue,
        "program": u,
        "modules": i[0]["module"]
    }

# print(days)

for k in days.keys():
    data = days[k]
    f = [l for l in data]
    ss = [data[d] for d in f]
    o = "program"
    for o in ss:
        print(o)
        """
        tunatakiwa tuwe na file ambalo lina save 
        izo module kwenye preogram usika
        """
