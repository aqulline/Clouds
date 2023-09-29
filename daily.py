import json


def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data


existing_data = load("ble.json")

time_slots = [
    "07:00-08:00", "08:00-08:30", "08:30-09:30", "09:30-10:00", "10:00-11:00", "11:00-11:30",
    "11:30-12:30", "12:30-13:00", "13:00-14:00", "14:00-14:30", "14:30-15:30", "15:30-16:00",
    "16:00-17:00", "17:00-17:30", "17:30-18:30"
]

day_of_week = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]

weeks = ["w1", "w2", "w3"]


days_of_week = [f"{j}{i}" for j in weeks for i in day_of_week]

# Print the formatted data
for program, modules in existing_data.items():
    for day in days_of_week:
        if day in modules:
            row = [day]
            for time_slot in time_slots:
                if time_slot in modules[day]:
                    row.append(modules[day][time_slot])
                else:
                    row.append("---")

count = "----"
with open("table.html", "w") as html_file:
    html_file.write("<html>\n")
    html_file.write("<head>\n")
    html_file.write("<title>Timetable</title>\n")
    html_file.write("</head>\n")
    html_file.write("<body>\n")
    html_file.write("<h1>NATIONAL INSTITUTE OF TRANSPORT TEST 2 TIMETABLE FOR ACADEMIC YEAR 2022_2023</h1>\n")

    # Iterate through programs and modules
    for program, modules in existing_data.items():
        html_file.write(f"<h2>{program}</h2>\n")
        html_file.write("<table border='1'>\n")


        # Write the table headers (time slots)
        html_file.write("<tr>\n")
        html_file.write("<th>Time/Day</th>\n")
        for time_slot in time_slots:
            html_file.write(f"<th>{time_slot}</th>\n")
        html_file.write("</tr>\n")

        for day in days_of_week:
            html_file.write("<tr>\n")
            html_file.write(f"<td>{day}</td>\n")
            for time_slot in time_slots:
                for k, h in modules.items():
                    dayss = h["day"]
                    week = h["week"]
                    time = h["time"]
                    if week+dayss == day and time == time_slot:
                        count = k
                html_file.write(f"<td>{count}</td>\n")
                count = "----"

            html_file.write("</tr>\n")
        count = "----"
        html_file.write("</table>\n")

    html_file.write("</body>\n")
    html_file.write("</html>\n")

print("Timetable HTML file created: timetable.html")

