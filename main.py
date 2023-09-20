import os
import re

from kivy.properties import NumericProperty, StringProperty, DictProperty, BooleanProperty, ListProperty
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy import utils
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField

from database import Database as DT
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
import string
import random

from kivymd.uix.picker import MDDatePicker
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine, \
    MDExpansionPanelTwoLine

Clock.max_iteration = 250
import json

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"


class Content(MDBoxLayout):

    gpa = "4"
    remark = "ok"

class NumberField(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):

        if len(self.text) == 0 and substring != "0":
            return

        if len(self.text) == 10:
            return

        if len(self.text) == 1 and substring != "6" and substring != "7":
            return

        if not substring.isdigit():
            return

        return super(NumberField, self).insert_text(substring, from_undo=from_undo)


class TNumberField(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):

        if len(self.text + substring) > 4:
            return

        if len(self.text) == 0 and substring != "T":
            return

        if len(self.text) > 0 and not substring.isdigit():
            return

        return super(TNumberField, self).insert_text(substring, from_undo=from_undo)


class DataCard(MDCard):
    icon = StringProperty("dog")
    name = StringProperty("Aqulline")
    amount = StringProperty("12,00")


class Tab(MDBoxLayout, MDTabsBase):
    pass


class More(MDCard):
    icon = StringProperty("")


class RowCard(MDCard):
    date = StringProperty("")
    icon = StringProperty("")
    name = StringProperty("")
    price = StringProperty("")


class Labels(MDLabel):
    pass


class Emergency(MDBoxLayout):
    pass


class CustomOneLineIconListItem(OneLineIconListItem, AsyncImage):
    icon = StringProperty()
    phone = StringProperty


if utils.platform != 'android':
    Window.size = (412, 732)

KV = '''
MDFloatLayout:

    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
'''


class MainApp(MDApp):
    size_x, size_y = NumericProperty(0), NumericProperty(0)
    data_name = StringProperty("chagua aina!")
    data_icon = StringProperty("exclamation")
    matumizi = DictProperty(DT.exp_list(DT()))

    set = StringProperty("In this example, we have a ScrollView that occupies the entire available space with size_hint: 1, 1. The do_scroll_x property is set to False to disable horizontal scrolling.\
Inside the ScrollView, we have a BoxLayout with a vertical orientation. We set the spacing and padding values to provide spacing and padding between the Foods widgets.\
Within the BoxLayout, you can manually add Foods widgets using their corresponding class names and assigning unique id values. In this example, we have added five Foods widgets with different id values (food1, food2, food3, food4, food5).\
By defining the Foods widgets inside the BoxLayout within the ScrollView, they will be displayed as a scrollable list.")

    # Medicine
    name = StringProperty("......................")
    quantity = StringProperty("......................")
    price = StringProperty("......................")
    expire = StringProperty("......................")

    sname = StringProperty("......................")
    squantity = StringProperty("......................")
    sprice = StringProperty("......................")
    sexpire = StringProperty("......................")

    date = StringProperty("Open date picker")

    amount = StringProperty("0")
    ramount = StringProperty("0")
    heigt = StringProperty("")

    gpa_s = [3.0, 3.9, 3.5, 2.7]


    def on_start(self):
        self.Exp()
        self.display_result()
        self.login_check()

    added_widgets = ListProperty([])

    def Exp(self):
        for i in range(self.gpa_s.__len__()):
            Content.gpa = str(self.gpa_s[i])
            Panel = MDExpansionPanel(
                    icon="BS.png",
                    content=Content(),
                    panel_cls=MDExpansionPanelTwoLine(
                        text=str(self.gpa_s[i]),
                        secondary_text="Secondary text",

                    )
                )
            self.root.ids.box.add_widget(Panel)
            self.added_widgets.append(Panel)

    def add_ddt(self):
        self.gpa_s.append(4.5)
        self.clear_map_widgets()
        self.Exp()

    def clear_map_widgets(self):
        map = self.root.ids.box
        for widget in self.added_widgets:
            map.remove_widget(widget)
        self.added_widgets.clear()


    def login_view(self):
        cd = self.root.ids.login_code
        lk = self.root.ids.locks
        lg = self.root.ids.view
        if cd.text == "0000":
            toast("Succes!")
            cd.password = False
            lk.icon = "lock-open-variant"
            lg.pos_hint = {'center_x': .65, 'center_y': .45}
        else:
            cd.password = True
            lk.icon = "lock"
            lg.pos_hint = {'center_x': .65, 'center_y': 2}



    def tranlat(self):
        from googletrans import Translator

        translator = Translator()

        # Translate a single sentence from English to French
        translation = translator.translate(self.set, src="en", dest="fr")
        print(translation.text)

        self.set = translation.text

    def tranlaten(self):
        from googletrans import Translator

        translator = Translator()

        # Translate a single sentence from English to French
        translation = translator.translate(self.set, src="fr", dest="en")
        print(translation.text)

        self.set = translation.text

    def id_generator(self):
        num = string.digits
        letter = string.ascii_letters

        rr = num + letter

        z = random.choice(rr)
        a = random.choice(rr)
        v = random.choice(rr)
        f = random.choice(rr)
        t = random.choice(rr)
        w = random.choice(rr)

        return z + a + v + f + t + w

    data = {'BusStops': {'Arusha': 'google-maps', 'Dar Es salaam': 'google-maps', 'Kilimanjaro': 'google-maps',
                         'Morogoro': 'google-maps', 'mabibo': 'google-maps', 'manzese': 'google-maps',
                         'marangu': 'google-maps', 'sokoni': 'google-maps'},
            'Details': {'car_name': 'Marangu Coach', 'car_plate_number': 'T657'},
            'Tracker': {'lat': -6.806236, 'lon': 39.2243981},
            'current_location': {'current': 'Dar Es salaam', 'prev': 'Stand Home'}}

    def fetch(self):
        data = self.data
        bus_stop = data['BusStops']
        track = data['Tracker']
        detail = data['Details']
        current_pos = data['current_location']
        self.bus_stp(bus_stop)
        m = self.root.ids.bus_detail
        he = Emergency()
        he.pos_hint = {"center_x": .5, "center_y": .9}
        he.name = detail['car_name']
        he.phone = detail['car_plate_number']
        he.call = "arrow-right-drop-circle"
        m.add_widget(he)

    def sms_scrn(self, name):
        sms = self.root
        sm = self.root.ids.name_stop
        sm.text = f"You will be notified when the bus reaches {name}"
        sms.current = "sms_stop"

    def category_sheet(self, data):
        bottom_sheet_menu = MDListBottomSheet()
        vimbweta = data
        count = 1
        for i in vimbweta.items():
            bottom_sheet_menu.add_item(
                i[0],
                lambda x, y=i[0], z=i[1]: self.callback_for_menu_items(y, z),
                icon=i[1],
            )
            count += 1
        bottom_sheet_menu.radius_from = 'top'
        bottom_sheet_menu.open()

    def callback_for_menu_items(self, y, z):
        toast(y)
        self.data_name = y
        self.data_icon = z

    def location_sheet(self, data):
        bottom_sheet_menu = MDListBottomSheet()
        vimbweta = data
        count = 1
        for i in vimbweta.items():
            bottom_sheet_menu.add_item(
                i[0],
                lambda x, y=i[0], z=i[1]: self.callback_for_menu_items(y, z),
                icon=i[1],
            )
            count += 1
        bottom_sheet_menu.radius_from = 'top'
        bottom_sheet_menu.open()

    def amount_update(self, num):
        if self.ramount == "0":
            self.ramount = num
            self.amount = num
        else:
            self.amount += num
            self.ramount = '{:,}'.format(int(self.amount))

    def delete(self):
        self.amount = self.ramount.replace(",", "")
        leng = len(self.amount) - 1
        self.amount = self.amount[0:leng]
        if self.amount == '':
            self.ramount = "0"
        else:
            self.amount = self.amount
            self.ramount = '{:,}'.format(int(self.amount))

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
    counter = 0

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

    def add_item(self, i, date=""):
        with open("data.json", "r") as f:
            data = json.load(f)
            try:
                main = data["data"]["20208"]["w12"][i]
                num = len(main)
                for i, y in main.items():
                    if self.counter < 3:
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
                    else:
                        if self.count == 0:
                            self.root.ids.customers.data.append(
                                {
                                    "viewclass": "More",
                                    "icon": "dots-horizontal"
                                }
                            )
                            self.count = + 1
                    self.counter = + 1

            except:
                self.root.ids.customers.data.append(
                    {
                        "viewclass": "Labels",
                        "text": "No Entry"
                    }
                )

    def login_auto(self):
        with open("user.json") as file:
            code = json.load(file)
            code = code["code"]
            cd = self.root.ids.code
            lk = self.root.ids.lock
            lg = self.root.ids.lgn
            if cd.text == code:
                toast("Succes!")
                cd.password = False
                lk.icon = "lock-open-variant"
                lg.pos_hint = {'center_x': .65, 'center_y': .45}

    def build(self):
        self.size_x, self.size_y = Window.size

        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "Orange"

    def on_save(self, instance, value, date_ranges):

        print(value)
        self.date = str(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def display_result(self):
        self.root.ids.result.data = {}
        history = {"Field Practical Training II", "Web Application Development", "Wei Application Development", "System Analysis and Design", "Object Oriented Programming", "Multimedia Concepts"}
        for i in history:
            self.root.ids.result.data.append(
                {
                    "viewclass": "ResultCard",
                    "name": i,


                }
            )

    def register_user(self, name, code):
        with open("user.json", "w") as file:
            data = {"user": name, "password": code}
            data_dump = json.dumps(data, indent=6)
            file.write(data_dump)
            file.close()
            sm = self.root
            #sm.current = "login_view"

    def login_check(self):
        file_size = os.path.getsize("user.json")
        if file_size == 0:
            sm = self.root
            #sm.current = "log"
        else:
            data = self.load("user.json")
            #self.user, self.user_password = data["user"], data["password"]
            sm = self.root
            #sm.current = "login_view"

    def load(self, data_file_name):
        with open(data_file_name, "r") as file:
            initial_data = json.load(file)
        return initial_data

MainApp().run()
