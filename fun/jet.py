class Agent:
    def __init__(self):
        self.total_cash_gain_ag1 = 0
        self.total_checkin_profit = 0
        self.total_cash_checkin = 0
        self.credits = 52500
        self.credits_amount = 52500
        self.amount_deposit = 0
        self.amount_checkout = 0
        self.previous_credit = 0
        self.credit_remain = 0
        self.credit_amount_for_current_transaction = 0
        self.amount_needed = 0
        self.total_deduction = 0
        self.cash_received = 0
        self.cash_gain = 0
        self.cash_gain_ag1 = 0
        self.total_cash_gain = 0
        self.total_checkout_profit = 0
        self.cash_checkout = 0
        self.total_cash_checkout = 0
        self.cash_checkin = 0
        self.agent_id = 0
        self.number_of_transaction = 0
        self.credits_profits = 0
        self.checkout_profits = 0
        self.checkin_profits = 0

        self.super_agent_profit = 0
        self.agent1_profit = 0
        self.agent2_profit = 0
        self.super_agent_debt = 0

        self.s_agent_profit = 0
        self.s_money_gain = 52500
        self.s_agent_loss = 0
        self.s_money_remain = 0

    def checkout_money(self, money):
        self.cash_checkout = self.amount_deposit
        self.checkout_profits = self.percent_profit(money) * 50 / 100
        self.total_checkout_profit = self.total_checkout_profit + self.checkout_profits
        self.cash_gain = self.cash_checkout + self.checkout_profits
        self.total_cash_gain = self.total_cash_gain + self.cash_gain
        self.total_cash_checkout = self.total_cash_checkout + self.cash_checkout
        print("\t \t \t \t \t \t \t \t AGENT2 LOGs!\t \t \t \t \t \t \t \t")
        print(f"'Agent2:' Money Current Cash out>> {self.cash_checkout}")
        print(f"'Agent2:' Current Cash out Profit>> {self.checkout_profits}")
        print(f"'Agent2:' Current Money Gain>> {self.cash_gain}")
        print(f"'Agent2:' Total Cash gain>> {self.total_cash_gain}")
        print(f"'Agent2:' Total Checkout profit>> {self.total_checkout_profit}")
        print(f"'Agent2:' Total Cash Checkout>> {self.total_cash_checkout} \n")
        self.super_profit(self.cash_gain)

    def checkin_money(self, money):
        self.cash_checkin = self.amount_deposit + self.percent_profit(money)
        self.checkin_profits = self.percent_profit(money) * 30 / 100
        self.checkout_profits = self.percent_profit(money) * 50 / 100
        self.super_agent_profit = self.percent_profit(money) * 30 / 100
        self.total_deduction = self.checkin_profits + self.super_agent_profit + self.checkout_profits
        self.credit_amount_for_current_transaction = self.percent_profit(
            money) + self.amount_deposit - self.checkin_profits
        self.previous_credit = self.credits
        self.amount_needed = self.percent_profit(money) + self.amount_deposit
        self.credit_remain = self.credits - self.credit_amount_for_current_transaction
        self.credits = self.credit_remain
        self.agent1_profit = self.amount_needed - self.credit_amount_for_current_transaction
        self.total_cash_checkin = self.total_cash_checkin + self.cash_checkin
        self.total_checkin_profit = self.total_checkin_profit + self.checkin_profits
        self.cash_gain_ag1 = self.amount_needed
        self.total_cash_gain_ag1 = self.cash_gain_ag1 + self.total_cash_gain_ag1
        print("\t \t \t \t \t \t \t \t AGENT1 LOGs!\t \t \t \t \t \t \t \t")
        print(f"'Agent1:' Money Current Cash checkin>> {self.cash_checkin}")
        print(f"'Agent1:' Current Cash Checkin Profit>> {self.checkin_profits}")
        print(f"'Agent1:' Money Deposited>> {self.amount_deposit}")
        print(f"'Agent1:' Previous Credit>> {self.previous_credit}")
        print(f"'Agent1:' Credit Remain>> {self.credit_remain}")
        print(f"'Agent1:' Credit amount for current Transaction>> {self.credit_amount_for_current_transaction}")
        print(f"'Agent1:' Amount For credits bought>> {self.credits_amount}")
        print(f"'Agent1:' Amount Gain for current Transaction>> {self.cash_gain_ag1}")
        print(f"'Agent1:' Total Amount again>> {self.total_cash_gain_ag1}")
        print(f"'Agent1:' Total Checkin Profit>> {self.total_checkin_profit}")
        print(f"'Agent1:' Total profit>> {(self.total_cash_gain_ag1 - self.credits_amount) + self.credit_remain} \n")
        self.checkout_money(money)

    def super_profit(self, money):
        self.s_money_remain = self.s_money_gain - money
        self.s_money_gain = self.s_money_remain
        print("\t \t \t \t \t \t \t \t SUPER AGENT LOGs!\t \t \t \t \t \t \t \t")
        print(f"'SUPER AGENT:' Total money gain>> {self.credits_amount}")
        print(f"'SUPER AGENT:' Total money remain>> {self.s_money_remain} \n")

    # Temporary Testing Simulator
    def scenario(self):
        while True:
            self.number_of_transaction += 1
            if self.credits >= 1000:
                self.amount_deposit = int(input("Enter Amount: "))
                self.checkin_money(self.amount_deposit)
            else:
                return False

    def percent_profit(self, amount):
        if 10_000 <= amount <= 19_999:
            money_remain = amount * 10 / 100
            self.amount_deposit = amount
            return money_remain

        elif 1000 <= amount <= 1999:
            money_remain = amount * 20 / 100
            self.amount_deposit = amount
            return money_remain

        elif 2000 <= amount <= 4999:
            money_remain = amount * 9 / 100
            self.amount_deposit = amount
            return money_remain

        elif 5000 <= amount <= 9999:
            money_remain = amount * 8 / 100
            self.amount_deposit = amount
            return money_remain

        elif 20_000 <= amount <= 39_999:
            money_remain = amount * 6 / 100
            self.amount_deposit = amount
            return money_remain

        elif 40_000 <= amount <= 59_999:
            money_remain = amount * 5 / 100
            self.amount_deposit = amount
            return money_remain


class SuperAgent_HQ:
    def __init__(self):
        self.total_amount = 0
        self.agents = []
        self.total_debt = 0
        self.total_profit = 0


class Customer:
    def __init__(self):
        self.cash = 0
        self.customer_id = 0


Agent.scenario(Agent())

money = [10000, 10000, 5000, 7000, 3000, 9000, 3000, 2000]
