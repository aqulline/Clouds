import json


class Database:

    def exp_list(self):
        with open("database/exp.json") as expenses:
            exp = json.load(expenses)

            return exp

# Database.date_format(Database())
# Database.data_input(Database(), "kitungu", "200", "income", "dog")
# Database.today_total(Database())
# Database.update_wallet(Database(), "airtel", "3000")

