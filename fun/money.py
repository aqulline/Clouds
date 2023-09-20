money = [390, 462, 704, 822, 1170, 1170, 1280, 1280, 1280, 2390]

more = [3990, 4310, 5700, 7400]

mon = 0

mone = 10_000

for ttl_deduction in money:
    mon = mon + 1000
    perc = f"{int(ttl_deduction * 100 / mon)}%"
    receive = mon - ttl_deduction
    agent = ttl_deduction * 0.5 / 100
    send = mon + ttl_deduction

for ttl_deduction in more:
    mone = mone + 10_000
    perc = f"{int(ttl_deduction * 100 / mone)}"
    agent = ttl_deduction * 0.5 / 100
    art = ttl_deduction - agent
    receive = mone - ttl_deduction
    send = mone + ttl_deduction

