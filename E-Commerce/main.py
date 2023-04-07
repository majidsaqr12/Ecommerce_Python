import pickle
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.toast import toast
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
    email = ""
    full_Name = ""

    def __init__(self):
        super().__init__()
        self.screen_mngr = None
        self.manager = None

    def build(self):
        self.title = "E Bay"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('mainApp.kv')

    def login(self):
        # self.email = self.root.ids.login_email.text
        self.root.ids.md_login.elevation = 4
        if self.root.ids.login_email.text == self.email and self.root.ids.login_email.text != "" and self.root.ids.login_email.text.__contains__(
                '@') and self.root.ids.login_email.text.__contains__('.com'):
            self.root.ids.email_intent.text = "Email :  " + self.email
            self.root.ids.name_intent.text = "Name : " + self.full_Name
            self.root.ids.screen_mngr.current = "home1"
            self.root.ids.login_email.text = ""
            self.root.ids.text_field.text = ""
            print(self.root.ids.login_pass.text)
            self.root.ids.login_pass.text = ""
            # kivymd.toast.kivytoast.kivytoast.toast("successfully", [], 10)
            toast('Successfully')
        else:
            toast('please enter correct email or password')
            self.root.ids.login_email.required = True
            self.root.ids.login_email.helper_text = "Please enter correct email"

    def sign_up(self):
        file = open("data.dot", "ab")
        self.email = self.root.ids.email_up.text
        self.full_Name = self.root.ids.full_name.text

        if self.email != "" and self.full_Name != "" and self.email.__contains__('@') and self.email.__contains__(
                '.com'):
            self.root.ids.screen_mngr.current = "home1"
            self.root.ids.email_intent.text = "Email :  " + self.email
            self.root.ids.name_intent.text = "Name : " + self.full_Name
            self.root.ids.email_up.text = ""
            self.root.ids.full_name.text = ""
            toast('Registration completed successfully, Thank you')
            pickle.dump(self.email, file)
            file.close()

        else:
            self.root.ids.email_up.required = True
            self.root.ids.email_up.helper_text = "example@gmail.com"
            self.root.ids.full_name.required = True
            toast('please complete your info')

    def sign_in_from_sign_up(self):
        self.root.ids.md_login.elevation = 4
        self.root.ids.screen_mngr.current = "home"


if __name__ == '__main__':
    MainApp().run()
