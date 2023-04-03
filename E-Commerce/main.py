from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (350, 600)

class My_Layout(FloatLayout):
    screen_mngr = ObjectProperty(None)


class Screen1(Screen):
    pass


class ClickableTextFieldRoundPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class ClickableTextFieldRoundEmail(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class Signup_Screen(Screen):
    pass


class MD_Bottom_Navigation_Screen(Screen):
    pass


class Fgt_pass_Screen(Screen):
    pass


class List_Laptop_Screen(Screen):
    pass


class List_phones_Screen(Screen):
    pass


class Show_Product_Lap_Screen(Screen):
    pass


class Show_Product_Lap1_Screen(Screen):
    pass


class Show_Product_Lap2_Screen(Screen):
    pass


class Show_Product_Lap3_Screen(Screen):
    pass


class Show_Product_Lap4_Screen(Screen):
    pass


class Show_Product_Lap5_Screen(Screen):
    pass


class Show_Product_phone_Screen(Screen):
    pass


class Show_Product_phone1_Screen(Screen):
    pass


class Show_Product_phone2_Screen(Screen):
    pass


class Show_Product_phone3_Screen(Screen):
    pass


class Show_Product_phone4_Screen(Screen):
    pass


class Show_Product_phone5_Screen(Screen):
    pass


class MainApp(MDApp):

    login_pass = ""

    def __init__(self, **kwargs):
        super().__init__()
        self.screen_mngr = None
        self.manager = None

    def build(self):
        self.title = "E Bay"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.9
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('mainApp.kv')

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def logger(self):
        x = "majid"
        self.root.ids.sign_up_field.text = x
        var = self.root.ids.passw

    def moving_home(self):
        self.root.ids.screen_mngr.current = "home1"
        # self.login_pass = self.root.screen_mngr.get_screen('home').ids.login_pass.text
        # print("this password : ", self.root.ids.screen_mngr.get_screen('home').ids.login_pass.text)


if __name__ == '__main__':
    MainApp().run()
