import json
import random
from time import sleep


def size_bl(c_s, s_s, data, vn, w_v_d_t, rnd_venue_list):
    prev = w_v_d_t
    while int(s_s) - int(c_s) > 15:
        rnd_venue_list = random.choice(data)
        print(len(rnd_venue_list))
        if len(rnd_venue_list) >= 10:
            w_v_d_t = random.choice(rnd_venue_list)
            vne = w_v_d_t.strip().split(";")[1]
            c_s = vn[vne]["size"]
            print(prev, "here", w_v_d_t)
            print(c_s, s_s)
            # sleep(1)
        else:
            pass
    return [w_v_d_t, rnd_venue_list]


def get_oode(name):
    code = ""
    for i in name:
        if not i.isdigit():
            code += i
        else:
            break
    return code


def get_size(text):
    import re

    pattern = r'^(.*?)\s*\((\d+)\)$'

    match = re.match(pattern, text)

    if match:
        extracted_text = match.group(1).strip()
        extracted_number = match.group(2)

        return extracted_number
    else:
        print("No match found.")


def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data


def write(data):
    with open("ble.json", "w") as file:
        initial_data = json.dumps(data, indent=4)
        file.write(initial_data)


chosed_techer_it = []


def get_teacher(teches, w, t, d, v):
    teach = f"{random.choice(teches)};{w};{t};{d};{v}"
    while teach in chosed_techer_it:
        teach = f"{random.choice(teches)};{w};{t};{d};{v}"
    return teach


it_teacher = [f"tit{i}" for i in range(1, 41)]

bba_teacher = [f"tbb{i}" for i in range(1, 41)]

vn100 = load("venues_100.json")
venues100 = [i for i in vn100.keys()]

vn10 = load("venues_10.json")
venues10 = [i for i in vn10.keys()]

vnb50 = load("venueb50.json")
venuesb50 = [i for i in vnb50.keys()]

vna50 = load("venuea50.json")
venuea50 = [i for i in vna50.keys()]

vna120 = load("venuea120.json")
venuea120 = [i for i in vna120.keys()]

vnb120 = load("venueb120.json")
venueb120 = [i for i in vnb120.keys()]

programes = load("module.json")

programmes = [i for i in
              programes.keys()]

modules = load("module.json")

modules_lits = [[modules[i][j].strip() for j in modules[i]]
                for i in modules]

weeks = ["w1",
         "w2", "w3"]
days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', "Saturday"]

times = ['07:00-08:00', '08:00-08:30', '08:30-09:30', '09:30-10:00', '10:00-11:00', '11:00-11:30', '11:30-12:30',
         '12:30-13:00', '13:00-14:00', '14:00-14:30', '14:30-15:30', '15:30-16:00', '16:00-17:00', '17:00-17:30',
         '17:30-18:30']

venue_day_time_100 = [[f"{h};{i};{k};{j}" for j in times] for k in days
                      for i in venues100 for h in weeks]

venue_day_time_10 = [[f"{h};{i};{k};{j}" for j in times] for k in days
                     for i in venues10 for h in weeks]

venue_day_time_b50 = [[f"{h};{i};{k};{j}" for j in times] for k in days
                      for i in venuesb50 for h in weeks]

venue_day_time_a50 = [[f"{h};{i};{k};{j}" for j in times] for k in days
                      for i in venuea50 for h in weeks]

venue_day_time_a120 = [[f"{h};{i};{k};{j}" for j in times] for k in days
                       for i in venuea120 for h in weeks]

venue_day_time_b120 = [[f"{h};{i};{k};{j}" for j in times] for k in days
                       for i in venueb120 for h in weeks]

timetable = {}

mph = []
for i in venue_day_time_a120:
    if "MPH" in i[0]:
        mph.append(i)

temp_listb50 = []
temp_lista50 = []
temp_listb120 = []
temp_lista120 = []


def append(list, name):
    list.clear()


dog = ""
cat = ""
cow = ""
pig = ""
for i in range(len(programmes)):
    pro = programmes[i]
    modd = modules_lits[i]

    for k in modd:
        modle = k
        Psize = get_size(pro)

        if int(Psize) < 40:
            prev_index = int
            data = venue_day_time_b50
            rnd_venue_list = random.choice(data)
            current_index = data.index(rnd_venue_list)
            current_pos = rnd_venue_list[0].strip().split(";")[2]
            while dog == current_pos:
                print(dog, current_pos)
                rnd_venue_list = random.choice(data)
                current_pos = rnd_venue_list[0].strip().split(";")[2]
                # sleep(5)
            dog = rnd_venue_list[0].strip().split(";")[2]
            w_v_d_t = random.choice(rnd_venue_list)
            Eweek = w_v_d_t.strip().split(";")[0]
            Evenue = w_v_d_t.strip().split(";")[1]
            Eday = w_v_d_t.strip().split(";")[2]
            Etime = w_v_d_t.strip().split(";")[3]
            Svenue = vnb50[Evenue]["size"]
            removed_day = data[data.index(rnd_venue_list)][rnd_venue_list.index(w_v_d_t)]
            remove_list = data[data.index(rnd_venue_list)]
            temp_listb50.append(data.index(rnd_venue_list))
            data[data.index(rnd_venue_list)].remove(removed_day)
            # data.remove(remove_list)
            code_init = get_oode(modle)
            teacherr = get_teacher(it_teacher, Eweek, Etime, Eday, Evenue)
            Eteacher = teacherr.strip().split(";")[0]
            chosed_techer_it.append(teacherr)

            if pro not in timetable:
                timetable[pro] = {}

            timetable[pro][modle] = {
                "venue": Evenue,
                "teacher": Eteacher,
                "day": Eday,
                "time": Etime,
                "week": Eweek,
                "module": modle,
                "program": pro,
                "students_size": Psize,
                "venue_size": Svenue
            }
        elif int(Psize) <= 70:
            data = venue_day_time_a50
            rnd_venue_list = random.choice(data)
            current_index = data.index(rnd_venue_list)
            current_pos = rnd_venue_list[0].strip().split(";")[2]
            while cat == current_pos:
                print(cat, current_pos)
                rnd_venue_list = random.choice(data)
                current_pos = rnd_venue_list[0].strip().split(";")[2]
                # sleep(5)
            cat = rnd_venue_list[0].strip().split(";")[2]
            w_v_d_t = random.choice(rnd_venue_list)
            Eweek = w_v_d_t.strip().split(";")[0]
            Evenue = w_v_d_t.strip().split(";")[1]
            Eday = w_v_d_t.strip().split(";")[2]
            Etime = w_v_d_t.strip().split(";")[3]
            Svenue = vna50[Evenue]["size"]
            removed_day = data[data.index(rnd_venue_list)][rnd_venue_list.index(w_v_d_t)]
            remove_list = data[data.index(rnd_venue_list)]
            temp_lista50.append(data.index(rnd_venue_list))
            data[data.index(rnd_venue_list)].remove(removed_day)
            # data.remove(remove_list)
            code_init = get_oode(modle)
            teacherr = get_teacher(it_teacher, Eweek, Etime, Eday, Evenue)
            Eteacher = teacherr.strip().split(";")[0]
            chosed_techer_it.append(teacherr)

            if pro not in timetable:
                timetable[pro] = {}

            timetable[pro][modle] = {
                "venue": Evenue,
                "teacher": Eteacher,
                "day": Eday,
                "time": Etime,
                "week": Eweek,
                "module": modle,
                "program": pro,
                "students_size": Psize,
                "venue_size": Svenue
            }
        elif int(Psize) <= 135:
            data = venue_day_time_b120
            rnd_venue_list = random.choice(data)
            current_index = data.index(rnd_venue_list)
            current_pos = rnd_venue_list[0].strip().split(";")[2]
            while cow == current_pos:
                print(cow, current_pos)
                rnd_venue_list = random.choice(data)
                current_pos = rnd_venue_list[0].strip().split(";")[2]
                # sleep(5)
            cow = rnd_venue_list[0].strip().split(";")[2]
            w_v_d_t = random.choice(rnd_venue_list)
            Eweek = w_v_d_t.strip().split(";")[0]
            Evenue = w_v_d_t.strip().split(";")[1]
            Eday = w_v_d_t.strip().split(";")[2]
            Etime = w_v_d_t.strip().split(";")[3]
            Svenue = vnb120[Evenue]["size"]
            removed_day = data[data.index(rnd_venue_list)][rnd_venue_list.index(w_v_d_t)]
            remove_list = data[data.index(rnd_venue_list)]
            temp_listb120.append(data.index(rnd_venue_list))
            data[data.index(rnd_venue_list)].remove(removed_day)
            # data.remove(remove_list)
            code_init = get_oode(modle)
            teacherr = get_teacher(it_teacher, Eweek, Etime, Eday, Evenue)
            Eteacher = teacherr.strip().split(";")[0]
            chosed_techer_it.append(teacherr)

            if pro not in timetable:
                timetable[pro] = {}

            timetable[pro][modle] = {
                "venue": Evenue,
                "teacher": Eteacher,
                "day": Eday,
                "time": Etime,
                "week": Eweek,
                "module": modle,
                "program": pro,
                "students_size": Psize,
                "venue_size": Svenue
            }
        elif int(Psize) > 120:
            data = venue_day_time_a120
            rnd_venue_list = random.choice(data)
            current_index = data.index(rnd_venue_list)
            current_pos = rnd_venue_list[0].strip().split(";")[2]
            while pig == current_pos:
                print(pig, current_pos)
                rnd_venue_list = random.choice(data)
                current_pos = rnd_venue_list[0].strip().split(";")[2]
                # sleep(5)
            pig = rnd_venue_list[0].strip().split(";")[2]
            w_v_d_t = random.choice(rnd_venue_list)
            Eweek = w_v_d_t.strip().split(";")[0]
            Evenue = w_v_d_t.strip().split(";")[1]
            Eday = w_v_d_t.strip().split(";")[2]
            Etime = w_v_d_t.strip().split(";")[3]
            Svenue = vna120[Evenue]["size"]
            removed_day = data[data.index(rnd_venue_list)][rnd_venue_list.index(w_v_d_t)]
            temp_lista120.append(data.index(rnd_venue_list))
            data[data.index(rnd_venue_list)].remove(removed_day)
            # data.remove(remove_list)
            code_init = get_oode(modle)
            teacherr = get_teacher(it_teacher, Eweek, Etime, Eday, Evenue)
            Eteacher = teacherr.strip().split(";")[0]
            chosed_techer_it.append(teacherr)

            if pro not in timetable:
                timetable[pro] = {}

            timetable[pro][modle] = {
                "venue": Evenue,
                "teacher": Eteacher,
                "day": Eday,
                "time": Etime,
                "week": Eweek,
                "module": modle,
                "program": pro,
                "students_size": Psize,
                "venue_size": Svenue
            }
    append(temp_listb50, "b50")
    append(temp_lista50, "a50")
    append(temp_lista120, "a120")
    append(temp_listb120, "b120")
    dog = ""
    cat = ""
    cow = ""
    pig = ""

# print(timetable)
write(timetable)
import updatert
