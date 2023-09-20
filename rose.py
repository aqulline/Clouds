import json

dat = ['532265', '6283230638', '9984164661', '731607', '45839520', '16806584', '532265', '19267043', '941611']
x = '532265'


def load(data_file_name):
    with open(data_file_name, "r") as file:
        initial_data = json.load(file)
    return initial_data



data = load("code.json")

sa = data.items()

worfd  = ""
words = []

for x in dat:
    leng = len(x)
    for i in range(1, int(leng / 2) + 1):
        print(i)
        mlt = i * 2
        code = x[mlt - 2:mlt]
        for i, u in sa:
            if u == code:
                print(i)
                worfd = worfd + i
    words.append(worfd)
    worfd = ""

print(words)
v = " ".join(words)
