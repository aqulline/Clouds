import json

matumizi = {
    "Chakula": "food",
    "Nauli": "van-passenger",
    "Maji": "water-pump",
    "Umeme": "electron-framework",
    "Taka": "trash-can",
    "Gas": "gas-cylinder",
    "Perfume": "air-filter",
    "Mafuta": "water",
    "Lotion": "lotion",
    "Viungo": "carrot",
    "Vocha": "instagram",
    "Nguo": "tshirt-v",
    "Viatu": "shoe-sneaker",
    "Girl Friend": "face-woman",
    "Boy Friend": "face",
    "Kopesha": "alert-minus"
}
aq = {"150": {"102": {"35": {"aq": "mbuya", "0788204": "mbuya"}}}}
matumizi.update(aq)


def write(k):
    with open("user.json", "w") as file:
        h = json.dumps(k, indent=6)
        file.write(h)


def load():
    with open("user.json", "r") as file:
        h = json.load(file)
    return h


def write_d(k):
    with open("data.json", "w") as file:
        h = json.dumps(k, indent=6)
        file.write(h)


def load_d():
    with open("data.json", "r") as file:
        h = json.load(file)
    return h


def update():
    h = load()
    ke = aq
    he = h["data"]
    h["data"].update(ke)
    write(h)


def update_month(month):
    h = load_d()
    ke = month

    h["data"].update(ke)
    write_d(h)


def update_week(month, week):
    h = load_d()
    ke = week
    h["data"][month].update(ke)
    write_d(h)


def update_day(month, week, day):
    h = load_d()
    ke = day
    h["data"][month][week].update(ke)
    write_d(h)


def update_data(month, week, day, data):
    h = load_d()
    ke = data
    h["data"][month][week][day].update(ke)
    write_d(h)


def update_all():
    m = "20207"
    w = "w12"
    date = "2020726"
    id = "20207291330159"
    data = {m: {
        w: {
            date: {
                id: {
                    "name": "nyanya",
                    "category": "exp",
                    "amount": "200",
                    "icon": "carrot",
                    "date": "2020-7-26"
                }
            }
        }}}
    h = load_d()
    if m in h["data"]:
        print("pass")
        if w in h["data"][m]:
            print("pass")
            if date in h["data"][m][w]:
                print("pass")
                if id in h["data"][m][w][date]:
                    print("pass")
                else:
                    print("fail")
                    data = data[m][w][date]
                    update_data(m, w, date, data)

            else:
                print("fail")
                day = data[m][w]
                update_day(m, w, day)
        else:
            print("fail")
            week = data[m]
            update_week(m, week)

    else:
        print("fail")
        update_month(data)


def today():
    with open("data.json", "r") as f:
        data = json.load(f)
        main = data["data"]["20208"]["w12"]["2020726"]
        lenn = len(main)
    for i, y in main.items():
        print(y["name"])


def percent_calc():
    max = 481200

    value = 23800

    perc = (value * 100) / max

    return "{:.1f}".format(perc)


def now_exp():
    exp = 0
    inc = 0
    with open("data.json", "r") as f:
        data = json.load(f)
        main = data["data"]["20208"]["w12"]["2020726"]
        for i, y in main.items():
            if y["category"] == "exp":
                exp = exp + int(y["amount"].replace(",", ""))
            else:
                inc = inc + int(y["amount"].replace(",", ""))


now_exp()
