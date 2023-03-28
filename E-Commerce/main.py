from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (350, 560)  # ( Width & Height )


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


class mainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.9
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('Style.kv')

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


if __name__ == '__main__':
    mainApp().run()
