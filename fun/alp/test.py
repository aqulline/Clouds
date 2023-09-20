from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.app import MDApp
import random

Window.keyboard_anim_args = {"d": .2, "t": "linear"}

Window.size = [420, 740]


class Test(MDApp):
    target = StringProperty("")
    ans1 = StringProperty("")
    ans2 = StringProperty("")
    ans3 = StringProperty("")
    ans4 = StringProperty("")
    ans5 = StringProperty("")


    one1 = random.randint(1, 12)
    one2 = random.randint(1, 12)
    one3 = random.randint(1, 12)
    one4 = random.randint(1, 12)
    one5 = random.randint(1, 12)

    def start(self, target):
        print("rand=", self.one5, self.one4, self.one3, self.one2, self.one1)

        total = self.one5 + self.one4 + self.one3 + self.one2 + self.one1

        print("total", total)
        self.error(target, total)

    def erro_plus(self, one5, one4, one3, one2, one1, error):
        one5 = one5 + int(int(error) / 5)
        one4 = one4 + int(int(error) / 5)
        one3 = one3 + int(int(error) / 5)
        one2 = one2 + int(int(error) / 5)
        one1 = one1 + int(int(error) / 5)

        self.ans1 = str(one1)
        self.ans2 = str(one2)
        self.ans3 = str(one3)
        self.ans4 = str(one4)
        self.ans5 = str(one5)

        print("error rand=", one5, one4, one3, one2, one1)

        total = one5 + one4 + one3 + one2 + one1

        print("total new", total)

    def erro_minus(self, one5, one4, one3, one2, one1, error):
        one5 = one5 - int(int(error) / 5)
        one4 = one4 - int(int(error) / 5)
        one3 = one3 - int(int(error) / 5)
        one2 = one2 - int(int(error) / 5)
        one1 = one1 - int(int(error) / 5)

        self.ans1 = str(one1)
        self.ans2 = str(one2)
        self.ans3 = str(one3)
        self.ans4 = str(one4)
        self.ans5 = str(one5)

        print("error rand=", one5, one4, one3, one2, one1)

        total = one5 + one4 + one3 + one2 + one1

        print("total new", total)

    def error(self, t, to):
        if to > int(t):
            error = to - int(t)
            print("error", error)
            self.erro_minus(self.one5, self.one4, self.one3, self.one2, self.one1, error)
        elif to < int(t):
            error = int(t) - to
            print("error", error)
            self.erro_plus(self.one5, self.one4, self.one3, self.one2, self.one1, error)
        else:
            return True


Test().run()
