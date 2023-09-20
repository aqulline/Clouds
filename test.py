import json

from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy import utils

if utils.platform != 'android':
    Window.size = (412, 732)


class DataCard(MDCard):
    icon = StringProperty("dog")
    name = StringProperty("Aqulline")
    amount = StringProperty("12,00")


class RowCard(MDCard):
    date = StringProperty("")
    icon = StringProperty("")
    name = StringProperty("")
    price = StringProperty("")


class More(MDCard):
    icon = StringProperty("")


class Test(MDApp):
    size_x, size_y = NumericProperty(0), NumericProperty(0)
    y = NumericProperty(0)

    def on_start(self):
        for i in range(5):
            self.add_item("2020726")

    def build(self):
        self.size_x, self.size_y = Window.size

    def add_item(self, i, date=""):
        with open("data.json", "r") as f:
            data = json.load(f)
            try:
                main = data["data"]["20208"]["w12"][i]
                for i, y in main.items():
                    self.root.ids.customers.data.append(
                        {
                            "viewclass": "RowCard",
                            "icon": y["icon"],
                            "name": y["name"],
                            "date": y["date"],
                            "price": y["amount"],
                            "id": i
                        }
                    )
            except:
                self.root.ids.customers.data.append(
                    {
                        "viewclass": "Labels",
                        "text": "No Entry"
                    }
                )

    def item(self, i):
        with open("data.json", "r") as f:
            data = json.load(f)
            main = data["data"]["20208"]["w12"][i]
            for i, y in main.items():
                self.root.ids.customers.data.append(
                    {
                        "viewclass": "RowCard",
                        "icon": y["icon"],
                        "name": y["name"],
                        "date": y["date"],
                        "price": y["amount"],
                        "id": i
                    }
                )
                break

    def add_customer_item(self, name="aqulline", image="C:/Users/DELL/PycharmProjects/Pocket/components/icons/lock.png",
                          phone="0788"):
        self.root.ids.customers.data.append(
            {
                "viewclass": "DataCard",
                "icon": "dog",
                "name": "Sex",
                "amount": "12,000"
            }
        )
    count = 0
    def add_c(self):
        idd = self.root.ids.customers.data
        sas = len(idd)
        print(sas)
        if sas >= 7:
            print("fuck you")
            count = 0
            if self.count == 0:
                self.root.ids.customers.data.append(
                    {
                        "viewclass": "More",
                        "icon": "dots-horizontal"
                    }
                )
                self.count = + 1
        else:
            self.add_customer_item()


Test().run()
