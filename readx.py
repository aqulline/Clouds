import csv
import json
import re

programe = ""
modul = 0

datax = {}


def get_pro(text):
    pattern = r'^(.*?)\s*\((\d+)\)$'

    # Use re.match to find the pattern in the text
    match = re.match(pattern, text)

    if match:
        return True
    else:
        return False


def write(data):
    with open("module.json", "w") as file:
        initial_data = json.dumps(data, indent=4)
        file.write(initial_data)


pro_lit = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday"]
# Open the CSV file for reading
with open('export.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Iterate through each row in the CSV file
    for row in reader:
        modules = []
        # `row` is a list representing the current row
        # You can access individual elements using indexing, e.g., row[0], row[1], etc.
        # Process the row as needed

        row = [i for i in row if i != " " and i != '']

        # print(row)  # This will print the current row as a list

        if len(row) == 1:
            programo = row[0].strip()
            # modul = 0
            pro_lit = []
            if get_pro(programo):
                if "(" in programo and "V" not in programo and programo[0] != "L" and "CLASS" not in programo and \
                        programo[
                            0] != "R" and "MPH" not in programo:
                    programe = programo
                    print(programe)
        if row:
            if row[0].strip().split(" ")[0] in days:
                row.remove(row[0])
                print(row)
                for i in row:
                    if len(i) > 12 and "X" not in i:
                        # print(i)
                        if programe not in datax:
                            datax[programe] = {}
                        modul += 1
                        # print(modul)
                        datax[programe][f"module{modul}"] = i
                        # print(datax[programe][f"module{modul}"])

print(datax)

write(datax)
