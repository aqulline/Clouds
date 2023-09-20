import datetime
import time
nowoy = datetime.datetime.now().date().year
nowom = datetime.datetime.now().date().month
exp_date = "2024-1-7"


def day_remain(exp_date):
    st = time.time()
    now = f"{nowoy}-{nowom}"

    m1 = int(now.strip().split("-")[1])

    m2 = int(exp_date.strip().split("-")[1])

    y1 = int(now.strip().split("-")[0])

    y2 = int(exp_date.strip().split("-")[0])

    yd = (y2 - y1) * 365

    ytm1 = 30 * m1

    ytm2 = 30 * m2

    v = ytm2 - ytm1 + yd

    ent = time.time()

    d = ent-st

    return v


day_remain(exp_date)
