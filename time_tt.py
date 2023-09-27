# Your existing code to define variables
exam_time = 2
start_time = 7
end_time = 18
departments = [f"D{x}" for x in range(1, 5)]
program = [[f"{i}p{p}" for p in range(len(departments))] for i in departments]
module = [[f"{j}m{m}" for m in range(len(i))] for i in program for j in i]
venues = [f"vn{i}" for i in range(1, 27)]
time_exam = [f"t{i}" for i in range(7, 19)]
days_exam = [f"J{i}" for i in range(1, 13)]
days_time = [[f"{i}t{k}" for k in range(7, 19)] for i in days_exam]

# Create a dictionary to store the timetable
# Your existing code up to creating the module list
# ...

# Create a dictionary to store the timetable
timetable = {}

# Iterate through each module
for module_name in module:
    # Convert module_name to a string
    module_name_str = ''.join(module_name)

    # Iterate through each day_exam (12 days)
    for day_exam in days_exam:
        # Iterate through each venue
        for venue in venues:
            # Iterate through each available time slot
            for i in range(len(days_time)):
                # Check if the venue is available for the entire exam_time (2 hours)
                if i + exam_time <= len(days_time[0]):
                    # Assign the module to the timetable
                    if module_name_str not in timetable:
                        timetable[module_name_str] = []
                    timetable[module_name_str].append({
                        "day_exam": day_exam,
                        "venue": venue,
                        "time_slot": days_time[days_exam.index(day_exam)][i:i + exam_time]
                    })
                    # Mark the time slots as occupied
                    for j in range(exam_time):
                        print(days_time[days_exam.index(day_exam)][i + j])
                        days_time[days_exam.index(day_exam)][i + j] = "occupied"

# Print the generated timetable
for module_name, exams in timetable.items():
    print(f"Module: {module_name}")
    for exam in exams:
        print(f"Day Exam: {exam['day_exam']}, Venue: {exam['venue']}, Time Slot: {exam['time_slot']}")

dataz = {
    "BAE (54)": {
        "AEU 08103 Engineering Management": {
            "venue": "vn5",
            "day": "Wednesday",
            "time": "15:30-16:00",
            "week": "w1",
            "module": "AEU 08103 Engineering Management",
            "program": "BAE (54)"
        },
        "AEU 08101 Automobile Design & Development": {
            "venue": "vn25",
            "day": "Tuesday",
            "time": "17:30-18:30",
            "week": "w2",
            "module": "AEU 08101 Automobile Design & Development",
            "program": "BAE (54)"
        },
        "AEU 08104 Environmental & Safety Engineering": {
            "venue": "vn5",
            "day": "Monday",
            "time": "08:30-09:30",
            "week": "w1",
            "module": "AEU 08104 Environmental & Safety Engineering",
            "program": "BAE (54)"
        },
        "AEU 08102 Engine Management": {
            "venue": "vn18",
            "day": "Tuesday",
            "time": "08:00-08:30",
            "week": "w2",
            "module": "AEU 08102 Engine Management",
            "program": "BAE (54)"
        }
    },
    "BAME (20)": {
        "GSU 08101V Research Methodology": {
            "venue": "vn24",
            "day": "Wednesday",
            "time": "08:00-08:30",
            "week": "w2",
            "module": "GSU 08101V Research Methodology",
            "program": "BAME (20)"
        }
    },
    "BATF STREAM A (200)": {
        "BAU 08101 Transport Costing and Finance\"": {
            "venue": "vn3",
            "day": "Friday",
            "time": "11:30-12:30",
            "week": "w2",
            "module": "BAU 08101 Transport Costing and Finance\"",
            "program": "BATF STREAM A (200)"
        }}
    }
