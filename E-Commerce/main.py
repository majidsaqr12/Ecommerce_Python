from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.toast import toast
import mysql.connector

Window.size = (350, 600)


class My_Layout(FloatLayout):
    screen_mngr = ObjectProperty(None)


class Screen1(Screen):
    pass


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


class Show_Product_lab(Screen):
    pass


class Show_Product_phone(Screen):
    pass


class MainApp(MDApp):
    email = ""
    full_Name = ""
    password = ""
    confirm_password = ""

    my_dp = mysql.connector.connect(
        host="localhost",
        user="majidsaqr",
        password="135790521Mm@",
        database="EBay"
    )

    cursor = my_dp.cursor()

    # cursor.execute("CREATE DATABASE EBay")
    # cursor.execute("CREATE TABLE DataUser(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

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
        if self.root.ids.login_email.text != "":
            if self.root.ids.login_email.text.__contains__('@'):
                if self.root.ids.login_email.text.__contains__('.com'):
                    if self.root.ids.login_email.text == self.email:
                        if self.password != "":
                            if self.root.ids.login_pass.text == self.password:
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
                                toast("Password is incorrect")
                        else:
                            toast("Missed Password")
                    else:
                        toast('Not valid email or password')
                        self.root.ids.login_email.required = True
                        self.root.ids.login_email.helper_text = "Not valid"
                else:
                    toast('Your email should contain .com')
            else:
                toast('Your email should contain @')
        else:
            toast('Missed email')

    def sign_up(self):
        self.email = self.root.ids.email_up.text
        self.full_Name = self.root.ids.full_name.text
        self.password = self.root.ids.sign_up_pass.text
        self.confirm_password = self.root.ids.sign_up_confirm_pass.text

        if self.full_Name != "":
            if self.full_Name.__contains__(' '):
                if self.email != "":
                    if self.email.__contains__('@'):
                        if self.email.__contains__('.com'):
                            if self.password != "":
                                if self.password.__contains__(min("8")):
                                    if self.confirm_password == self.password:
                                        self.root.ids.screen_mngr.current = "home1"
                                        self.root.ids.email_intent.text = "Email :  " + self.email
                                        self.root.ids.name_intent.text = "Name : " + self.full_Name
                                        self.root.ids.email_up.text = ""
                                        self.root.ids.full_name.text = ""
                                        toast('Registration completed successfully')
                                        sql = "INSERT INTO DataUser (name, email, password) VALUES (%s, %s, %s)"
                                        val = (self.full_Name, self.email, self.password)
                                        self.cursor.execute(sql, val)
                                        self.my_dp.commit()
                                        self.my_dp.close()
                                    else:
                                        toast("passwords are not same")
                                else:
                                    toast("Password must contain 8 characters")
                            else:
                                toast("Password is missed")
                        else:
                            toast('Your email should contain .com')
                    else:
                        toast('Your email should contain @')
                else:
                    toast('Email is missed')
            else:
                toast('Your name should contain first name and last name')
        else:
            toast('Name is missed')

    def sign_in_from_sign_up(self):
        self.root.ids.md_login.elevation = 4
        self.root.ids.screen_mngr.current = "home"

    def Add_success(self):
        toast("Add successfully")

    def skip(self):
        self.root.ids.screen_mngr.current = "home1"

    def change_product_lab1(self):
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap.jpg"
        self.root.ids.image_product.size_hint_x = 0.9 + 0.9 + 0.9
        self.root.ids.details_product.text = "HP 255 G8 Laptop - Ryzen 5 3500U, 8GB RAM, 1 TB HDD, AMD Radeon Vega, 8Graphics, 15.6-Inch HD, DOS - Asteroid, silver"
        self.root.ids.price_product.text = "Price  EGP12,463.62"

    def change_product_lab2(self):
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap2.png"
        self.root.ids.image_product.size_hint_x = 0.9 + 0.9
        self.root.ids.image_product.size_hint_y = 0.9 + 0.9
        self.root.ids.details_product.text = "Apple 32″ Pro Display XDR 16:9\nRetina 6K HDR IPS Display"
        self.root.ids.price_product.text = "Price  229,999 EGP"

    def change_product_lab3(self):
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap3.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.6
        self.root.ids.details_product.text = "Asus Vivobook 15 K513EP-BQ311T\nIntel® Core™ i5-1135G7-8GB-\n512GBSSD-NVIDIA® GeForce® MX330"
        self.root.ids.price_product.text = "Price  54,049 EGP"

    def change_product_lab4(self):
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap4.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.9
        self.root.ids.image_product.radius = 36, 36, 0, 0
        self.root.ids.details_product.text = "Lenovo Legion 5 Pro Core-i7-11800H, 32GB, 1TB SSD, RTX 3060 6GB,\n16WQXGA-2560 x 1600 - 500nits 165Hz"
        self.root.ids.price_product.text = "Price  35,7749 EGP"

    def change_product_lab5(self):
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap5.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.6
        self.root.ids.image_product.radius = 36, 36, 0, 0
        self.root.ids.details_product.text = "G15 5511 Gaming Laptop - Intel Core I7-11800H - RAM16GB - HARD 512GB\nSSD - VGA NVIDIA GeForce RTX 3050"
        self.root.ids.price_product.text = "Price  331,999 EGP"

    def change_product_lab6(self):
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap6.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.9
        self.root.ids.image_product.radius = 36, 36, 0, 0
        self.root.ids.details_product.text = "Dell G15-5520 Core-i7-12700H-14Core\n12Gen, 16GB-4800Mhz, 512GB SSD, RTX\n3050 4GB, 15.6FHD-120Hz, Backlit-A/E"
        self.root.ids.price_product.text = "Price  33,999 EGP"

    def change_product_phone1(self):
        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.9
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = "Apple iPhone 14 Pro Max 6.7-inch 5G"
        self.root.ids.price_product_phone.text = "Special Price  54,999.00 EGP"

    def change_product_phone2(self):
        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone1.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.9 + 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = "Google Pixel 7 Pro Single Sim, 5G, 12GB\nRam, 256GB, Snow, US Version"
        self.root.ids.price_product_phone.text = "Price  34,438 EGP"

    def change_product_phone3(self):
        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone2.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = "SAMSUNG 512GB 12GB RAM, Snapdragon 8 Gen 1 Galaxy S22 Ultra, 5G Phantom Black"
        self.root.ids.price_product_phone.text = "Price  41,999 EGP"

    def change_product_phone4(self):
        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone3.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = "Samsung Galaxy Tab S8 plus 12.4, Inches, 256 GB, 8 GB RAM, 5G LTE - Pink, Gold"
        self.root.ids.price_product_phone.text = "Price  44,433 EGP"

    def change_product_phone5(self):
        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone4.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = "Oppo Reno7 - 5G LTE, 256GB, 8GB RAM - Starry Black"
        self.root.ids.price_product_phone.text = "Price  18,850 EGP"

    def change_product_phone6(self):
        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone5.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = "ZTE Nubia Red magic 8 pro Dual Sim Matte\n12GB RAM 256GB 5G - International"
        self.root.ids.price_product_phone.text = "Price  28,950 EGP"


if __name__ == '__main__':
    MainApp().run()
