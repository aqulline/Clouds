import json

def decode(data):
    dats = data.strip().split("code")
    word = ""
    words = []
    codes = load("code.json")
    
    
    item = codes.items()

    for x in dats:
        leng = len(x)
        for i in range(1, int(leng / 2) + 1):
            print(i)
            mlt = i * 2
            code = x[mlt - 2:mlt]
            for i, u in item:
                if u == code:
                    print(i)
                    word = word + i
        words.append(word)
        word = ""
    return " ".join(words)


def load(data_file_name):
    with open(data_file_name, "r") as file:
        initial_data = json.load(file)
    return initial_data


data = load("code.json")

code = "the quick brown fox jump over the lazy dog"

sent = []

sentc = ""

for i in code:
    print(i)
    if i == " ":
        i = "letter"
    codes = data[i]
    sentc = sentc + codes

print(sentc)

decode(sentc)


