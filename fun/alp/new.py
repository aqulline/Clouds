from datetime import datetime

exp = "2023-10"


def remain_date(exp):
    nowoy = datetime.now().date().year
    nowom = datetime.now().date().month

    now = f"{nowoy}-{nowom}"

    m1 = int(now.strip().split("-")[1])

    m2 = int(exp.strip().split("-")[1])

    y1 = int(now.strip().split("-")[0])

    y2 = int(exp.strip().split("-")[0])

    yd = (y2 - y1) * 365

    ytm1 = 30 * m1

    ytm2 = 30 * m2

    total_days = ytm2 - ytm1 + yd

    if total_days >= 1 <= 30:
        print("Nearly to expired, remain days:", total_days, "to expire")

    elif total_days <= 0:
        print("Product expired, remain days:", total_days)


remain_date(exp)


kon = [x for x in range(1, 31)]

