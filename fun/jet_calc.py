prft = 0

amount = 50_000


def agents(money):
    agient1 = money * 50 / 100
    agient2 = money * 30 / 100
    supag = money * 20 / 100
    gv = supag * 18 / 100
    sup_ttl = supag - gv
    crd_amnt = money + amount - agient2
    money_to_send = amount + agient1 + supag + agient2
    ttl_deduction = agient2 + agient1 + supag
    money_agient2_to_pay_for_credits_for_a_particular_amount = amount
    profit_for_agient2 = agient2
    profit_for_agient1 = agient1
    profit_for_Super = sup_ttl
    agient2_prft = money_to_send - crd_amnt
    agient1_prft = amount + agient1
    super_agnt = crd_amnt + supag

    cmp_prft = super_agnt - agient1_prft


if 10_000 <= amount <= 19_999:
    perc = amount * 10 / 100
    agents(perc)

elif 1000 <= amount <= 1999:
    per = amount * 20 / 100
    agents(per)

elif 2000 <= amount <= 4999:
    per = amount * 9 / 100
    agents(per)

elif 5000 <= amount <= 9999:
    per = amount * 8 / 100
    agents(per)

elif 20_000 <= amount <= 39_999:
    per = amount * 6 / 100
    agents(per)

elif 40_000 <= amount <= 49_999:
    per = amount * 5 / 100
    agents(per)

elif 50_000 <= amount <= 89_999:
    per = amount * 5 / 100
    agents(per)

elif 90_000 <= amount <= 99_999:
    per = amount * 4 / 100
    agents(per)

elif 100_000 <= amount <= 199_999:
    per = amount * 5 / 100
    agents(per)
