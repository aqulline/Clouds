if int(Psize) >= 100:

    rnd_venue_list = random.choice(venue_day_time_100)
    w_v_d_t = random.choice(rnd_venue_list)
    Eweek = w_v_d_t.strip().split(";")[0]
    Evenue = w_v_d_t.strip().split(";")[1]
    Eday = w_v_d_t.strip().split(";")[2]
    Etime = w_v_d_t.strip().split(";")[3]
    Svenue = vn100[Evenue]["size"]
    removed_day = venue_day_time_100[venue_day_time_100.index(rnd_venue_list)][rnd_venue_list.index(w_v_d_t)]
    venue_day_time_100[venue_day_time_100.index(rnd_venue_list)].remove(removed_day)
    code_init = get_oode(modle)
    teacherr = get_teacher(it_teacher, Eweek, Etime, Eday, Evenue)
    Eteacher = teacherr.strip().split(";")[0]
    chosed_techer_it.append(teacherr)

    if int(Psize) - int(Svenue) > 10:
        w_v_d_t = venue_day_time_100[venue_day_time_100.index(rnd_venue_list)][
            rnd_venue_list.index(w_v_d_t) + 1]
        Evenue2 = w_v_d_t.strip().split(";")[1]

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
else:
    rnd_venue_list = random.choice(venue_day_time_10)
    w_v_d_t = random.choice(rnd_venue_list)
    Eweek = w_v_d_t.strip().split(";")[0]
    Evenue = w_v_d_t.strip().split(";")[1]
    Eday = w_v_d_t.strip().split(";")[2]
    Etime = w_v_d_t.strip().split(";")[3]
    Svenue = vn10[Evenue]["size"]

    removed_day = venue_day_time_10[venue_day_time_10.index(rnd_venue_list)][rnd_venue_list.index(w_v_d_t)]
    venue_day_time_10[venue_day_time_10.index(rnd_venue_list)].remove(removed_day)
    code_init = get_oode(modle)
    teacherr = get_teacher(it_teacher, Eweek, Etime, Eday, Evenue)
    Eteacher = teacherr.strip().split(";")[0]
    chosed_techer_it.append(teacherr)

    if int(Psize) - int(Svenue) > 10:
        w_v_d_t = random.choice(rnd_venue_list)
        w_v_d_n = f"{w_v_d_t.strip().split(';')[0]};{w_v_d_t.strip().split(';')[1]};{w_v_d_t.strip().split(';')[2]};{Etime}"
        Evenue2 = w_v_d_t.strip().split(";")[1]

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