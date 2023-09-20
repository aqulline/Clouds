secret = "SDoneR+ShucM3YVFWF9B/Yd8bDnxFjv385GUxXMOl68o9tw0qDJRu0ncfo8OvH7iex3hTAHdfjjqB8QnyvC7L6COSKoJuZ+ojmAj1fg7qaQYzCefhG2WOYbvbYOOkXuwWMiQgrrExFP6REwoOobXBf6VP8amk2v+XAIkyNbr2V6a1KFW1knzayWxD/KrcS2yn51aCVDuvDpnTjonDZ7/qQX0zfpGAZE23mfwE7UwpMZhxmnW9z0TjymSDi3oENY6iR7CTlzNcjdTzrHSfsxSELhrpDdhcOUgNTe3/hL8eIWV7/aDQy8UUVyuy/8WnmLVTUFKdjS9cwMcgsyn27WfVqrFPlrHllxyoO8909d3fu31fZxCAOLU7C6+0CGAamGY6eJ7/3DezPlmKiysbB4u0R05nmFkANXxcUI+Dyf1RQHtQfybjvICwrU8cSU2+RQlyClpts2Tw5XLNKff7nsECqMG4wOfzqCCpX3DVX5J71JiGiKjxebSslod34cWpqlhHmeTOE5+sbGBCPf0gj64plGsh+Qf/ejMxb4e8BH7G5YrFGuziDEY/FNGIa9lQZWnC/gqNVBXciRazRXTMvBascUbSWLTSQ1FPp7ThqpLrx9DEYnUDSjtgmv9dHl9/gS78ZLVik9zW9ZZ7sEMO+P0/VfHdpUPMlfSawq5AgiFw7w="

data = {
    "1_Invoice for Academic Year : 2020/2021": {
        "1": {
            "S/No": "1",
            "Pick": "",
            "nvoiceNo": "NIT3N2803",
            "Control Number": "995470072623",
            "Description": "Tuition and Administrative Fee",
            "Payment Mode": "PARTIAL",
            "Currency": "TZS",
            "Invoice": "1,000,000.00",
            "Amount": "1,000,000.00",
            "Paid": "0.00"
        }
    },
    "2_Invoice for Academic Year : 2020/2021": {
        "2": {
            "S/No": "2",
            "Pick": "",
            "nvoiceNo": "NIT3W2804",
            "Control Number": "995470072624",
            "Description": "NHIF",
            "Payment Mode": "PARTIAL",
            "Currency": "TZS",
            "Invoice": "50,400.00",
            "Amount": "50,400.00",
            "Paid": "0.00"
        }
    },
    "1_Invoice for Academic Year : 2021/2022": {
        "1": {
            "S/No": "1",
            "Pick": "",
            "nvoiceNo": "NT1010219820",
            "Control Number": "995470143922",
            "Description": "Tuition fee",
            "Payment Mode": "PARTIAL",
            "Currency": "TZS",
            "Invoice": "1,000,000.00",
            "Amount": "1,000,000.00",
            "Paid": "0.00"
        }
    },
    "1_Invoice for Academic Year : 2022/2023": {
        "1": {
            "S/No": "1",
            "Pick": "",
            "nvoiceNo": "NT1010231359",
            "Control Number": "995470214172",
            "Description": "Tuition fee",
            "Payment Mode": "PARTIAL",
            "Currency": "TZS",
            "Invoice": "1,000,000.00",
            "Amount": "1,000,000.00",
            "Paid": "0.00"
        }
    }
}

ylist = []


def get_yera(data):
    return data.strip().split(":")[1]


for i, y in data.items():
    year = get_yera(i)

    if year.strip() not in ylist:
        ylist.append(year.strip())


def get_year_data(years='2020/2021'):
    for x, z in data.items():
        if years == get_yera(x).strip():
            print(x)

get_year_data()