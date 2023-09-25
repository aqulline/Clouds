import json
import random


def write(data):
    with open("time.json", "w") as file:
        initial_data = json.dumps(data, indent=4)
        file.write(initial_data)

def randcc(day_t):
    chic = random.choice(day_t)
    length = day_t.__len__()
    indexx = day_t.index(chic)
    while day_t.index(chic) >= length or day_t.index(chic) >= length - 2:
        chic = random.choice(day_t)

    return chic


def venuex(list1, list2):
    while not list1:
        venue_r = random.choice(list2)

        list1 = venue_r

    return list1


def get_venue(venue):
    vn = ""
    for i in venue:
        if i == "v":
            vn = i + venue[venue.index(i) + 1] + venue[venue.index(i) + 2] + venue[venue.index(i) + 3]
    return vn


exam_time = 2

start_time = 7

end_time = 18

departments = [f"D{x}" for x in range(1, 11)]

program = [[f"{i}p{p}" for p in range(len(departments))] for i in departments]

module = [[f"{j}m{m}" for m in range(len(i))] for i in program for j in i]

venues = [f"vn{i}" for i in range(1, 27)]

time_exam = [f"t{i}" for i in range(7, 19)]

days_exam = [f"J{i}" for i in range(1, 13)]

days_time = [[f"{i}t{k}" for k in range(7, 19)] for i in days_exam]

venue_day_time = [[f"{i}{k}{j}" for j in time_exam] for k in days_exam for i in venues]

dictiom = {"D1p0": {"D1p0m0": {"venue": "vn1", "day": "j2", "time_in": "j2t7", "time_out": "j2t9"}}}

day_venu_time = []

timetable = {}

print(len(departments))
print(len(program))
print(len(module))
print(len(module) * len(program))

for i in days_exam:
    d_v_t = []
    for k in venues:
        vt = [f"{i}{k}{j}" for j in time_exam]
        d_v_t.append(vt)
    day_venu_time.append(d_v_t)

for i in program:
    for j in i:
        program = j
        pm = module[i.index(j)]
        for k in pm:
            modules = k
            day = random.choice(days_exam)
            day_t = day_venu_time[days_exam.index(day)]
            venue_r = venuex(random.choice(day_t), day_t)
            venue_time = randcc(venue_r)
            venue = get_venue(venue_time)
            time_in = venue_time
            #print(f"{program}:{modules}")
            time_out = day_venu_time[day_venu_time.index(day_t)][day_t.index(venue_r)][venue_r.index(venue_time) + 2]
            time_still = day_venu_time[day_venu_time.index(day_t)][day_t.index(venue_r)][venue_r.index(venue_time) + 1]
            day_venu_time[day_venu_time.index(day_t)][day_t.index(venue_r)].remove(time_in)
            day_venu_time[day_venu_time.index(day_t)][day_t.index(venue_r)].remove(time_out)
            day_venu_time[day_venu_time.index(day_t)][day_t.index(venue_r)].remove(time_still)
            #dictiom = {program: {modules: {"venue": venue, "day": day, "time_in": time_in, "time_out": time_out}}}
            #print(dictiom)
            if program not in timetable:
                timetable[program] = {}

            timetable[program][modules] = {
                "venue": venue,
                "day": day,
                "time_in": time_in,
                "time_out": time_out,
                "module":modules,
                "program": program,
            }
            #print(timetable[program][modules])
print(timetable)
print(len(timetable))

write(timetable)

