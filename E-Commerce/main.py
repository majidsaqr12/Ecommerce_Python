from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

from kivymd.app import MDApp

from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout

from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout


Window.size = (350, 560)  # ( Width & Height )


class My_Layout(FloatLayout):
    screen_mngr = ObjectProperty(None)


class ClickableTextFieldRoundPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class ClickableTextFieldRoundEmail(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


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


if __name__ == '__main__':
    mainApp().run()
