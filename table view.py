from prettytable import PrettyTable
import json
from colorama import Fore, Style
#import trued

def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data


# Your JSON data
timetable_json = load("ble.json")

# Initialize a PrettyTable
table = PrettyTable()

check_repetion = []

repeated = []

removed_day = 'w1;vn32;Saturday;11:30-12:30'

# Define the table headers
table.field_names = ["Program", "Module", "Teacher", "Venue", "Day", "Time", "Week"]

# Iterate through the JSON data and add rows to the table with colors

count = 0
for program, modules in timetable_json.items():
    for module, details in modules.items():
        day = Fore.RED + details["day"] + Style.RESET_ALL  # Color the "Day" column red
        time = details["time"]
        week = details["week"]
        teacher = details["teacher"]
        St = details["students_size"]
        Sv = details["venue_size"]
        if int(St) - int(Sv) > 20:
            venue = Fore.RED + details["venue"] + Style.RESET_ALL
            table.add_row([program, module, teacher, venue, day, time, week])

            v_d = week + venue + day + time + teacher

            count += 1

            if v_d in check_repetion:
                repeated.append(v_d)
            else:
                check_repetion.append(v_d)
        else:
            venue = details["venue"]
            table.add_row([program, module, teacher, venue, day, time, week])

            v_d = week + venue + day + time + teacher

            if v_d in check_repetion:
                repeated.append(v_d)
            else:
                check_repetion.append(v_d)

# Print the table
print(table)
print(len(repeated))
print(count)
