import random

import mysql.connector
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.toast import toast
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDRoundFlatButton, MDFlatButton, MDRaisedButton
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.snackbar import Snackbar

Window.size = (350, 600)


class MDSmartTileHover(MDSmartTile, HoverBehavior):
    def on_enter(self, *args):
        image_list = ["change_image/back1.jpg", "change_image/back2.jpg", "change_image/back3.jpg",
                      "change_image/back4.jpg", "change_image/back5.jpg", "change_image/back6.jpg"]
        self.source = random.choice(image_list)

    def on_leave(self, *args):
        pass


class MDSmartTileHover2(MDSmartTile, HoverBehavior):
    def on_enter(self, *args):
        image_list_phone = ["change_image_phone/phone1.jpg", "change_image_phone/phone2.jpg", "imgs/phones.png"]
        self.source = random.choice(image_list_phone)

    def on_leave(self, *args):
        pass


class MDFloatingActionButtonHover(MDFloatingActionButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = "E8A0BF"

    def on_leave(self, *args):
        self.md_bg_color = "ff0000"


class MDIconButtonHover(MDIconButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = "E8A0BF"

    def on_leave(self, *args):
        self.md_bg_color = "ff0000"


class MDRoundFlatButtonHover(MDRaisedButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = "E8A0BF"
        self.text_color = "#FFFFFF"

    def on_leave(self, *args):
        self.md_bg_color = "DDDDDD"
        self.text_color = "red"
        self.elevation = 3


class MDRoundFlatButtonHoverCart(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = "red"
        self.md_bg_color = "F9F54B"

    def on_leave(self, *args):
        self.text_color = "black"
        self.md_bg_color = "yellow"


class MDRoundFlatButtonHoverBuy(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = "red"
        self.md_bg_color = "F9F54B"

    def on_leave(self, *args):
        self.text_color = "black"
        self.md_bg_color = "orange"


class MDFlatButtonHover(MDFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = "red"

    def on_leave(self, *args):
        self.text_color = "orange"


class MDFlatButtonHoverWelcome(MDFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = "red"

    def on_leave(self, *args):
        self.text_color = "orange"


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


class Confirm_Screen(Screen):
    pass


class MainApp(MDApp):

    # ( Variables User Sign Up )
    email = ""
    full_Name = ""
    password = ""
    confirm_password = ""
    phone = ""
    # ( Variables Cart )
    amount_product = 0
    select_product = ""
    price_product = ""
    current_name = ""
    current_phone = ""
    date = ""

    my_dp = mysql.connector.connect(
        host="localhost",
        user="majidsaqr",
        password="135790521Mm@",
        database="EBay"
    )

    cursor = my_dp.cursor()

    my_dp_products = mysql.connector.connect(
        host="localhost",
        user="majidsaqr",
        password="135790521Mm@",
        database="EBay"
    )

    cursor_products = my_dp_products.cursor()

    # cursor.execute("CREATE DATABASE EBay") cursor.execute("CREATE TABLE Orders_Buy(id INT AUTO_INCREMENT PRIMARY
    # KEY, product VARCHAR(255), price VARCHAR(255), Fname VARCHAR(255), Lname VARCHAR(255), phone VARCHAR(255),
    # Sphone VARCHAR(255), state VARCHAR(255), city VARCHAR(255), street VARCHAR(255), Ddate VARCHAR(255),
    # amount VARCHAR(255))") cursor.execute("CREATE TABLE Cart(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),
    # email VARCHAR(255), phone VARCHAR(255), product VARCHAR(255), price VARCHAR(255), amount VARCHAR(255),
    # delivery_time VARCHAR(255))") cursor.execute("CREATE TABLE Cart_ID_Number(id INT AUTO_INCREMENT PRIMARY KEY,
    # ID_Number VARCHAR(255))") cursor.execute("CREATE TABLE DataUser(id INT AUTO_INCREMENT PRIMARY KEY,
    # name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255),password VARCHAR(255))")

    def __init__(self):
        super().__init__()
        self.screen_mngr = None
        self.manager = None

    def build(self):
        self.title = "E Bay"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('mainApp.kv')

    def on_start(self):
        pass

    def login(self):

        self.email = self.root.ids.login_email.text
        self.password = self.root.ids.login_pass.text

        check_info = False

        cursor2 = self.my_dp.cursor(dictionary=True)
        sql_select_query = "select * from DataUser"
        cursor2.execute(sql_select_query)
        records = cursor2.fetchall()

        for row in records:
            n = row["name"]
            p = row["phone"]
            e = row["email"]
            x = row["password"]
            if self.email == e and self.password == x:
                self.current_name = n
                self.current_phone = p
                check_info = True

        if self.root.ids.login_email.text != "":
            if self.root.ids.login_email.text.__contains__('@'):
                if self.root.ids.login_email.text.__contains__('.com'):
                    if self.password != "":
                        if check_info:
                            self.root.ids.screen_mngr.current = "home1"
                            self.root.ids.login_email.text = ""
                            self.root.ids.text_field.text = ""
                            self.root.ids.login_pass.text = ""
                            toast('Successfully')
                        else:
                            toast("Password or email is incorrect")
                    else:
                        toast("Missed Password")
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
        self.phone = self.root.ids.phone.text

        count_num = 0
        for _ in self.phone:
            count_num = count_num + 1

        check_email_founded = True

        cursor3 = self.my_dp.cursor(dictionary=True)
        sql_select_query = "select * from DataUser"
        cursor3.execute(sql_select_query)
        records = cursor3.fetchall()

        for row in records:
            e = row["email"]
            if self.email == e:
                check_email_founded = False

        if self.full_Name != "":
            if self.full_Name.__contains__(' '):
                if self.email != "":
                    if self.email.__contains__('@'):
                        if self.email.__contains__('.com'):
                            if check_email_founded:
                                if self.phone != "":
                                    if count_num == 13:
                                        if self.password != "":
                                            if self.confirm_password == self.password:
                                                self.root.ids.screen_mngr.current = "home"
                                                self.root.ids.email_up.text = ""
                                                self.root.ids.full_name.text = ""
                                                self.root.ids.sign_up_pass.text = ""
                                                self.root.ids.sign_up_confirm_pass.text = ""
                                                toast('Registration completed successfully')
                                                sql = "INSERT INTO DataUser (name, email, phone, password) VALUES (" \
                                                      "%s, %s, %s, %s)"
                                                val = (self.full_Name, self.email, self.phone, self.password)
                                                self.cursor.execute(sql, val)
                                                self.my_dp.commit()
                                                # self.my_dp.close()
                                            else:
                                                toast("passwords are not same")
                                        else:
                                            toast("Password is missed")
                                    else:
                                        toast("Phone is not valid")
                                else:
                                    toast("Phone is missed")
                            else:
                                toast("The email already exists")
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

    def change_product(self, product_id, image, screen):

        sql_query_product = "select product from Products where id =%s"
        id_ = (product_id,)
        self.cursor_products.execute(sql_query_product, id_)
        record = self.cursor_products.fetchone()
        lab = str(record[0])

        sql_query_product = "select price from Products where id =%s"
        id_ = (product_id,)
        self.cursor_products.execute(sql_query_product, id_)
        record = self.cursor_products.fetchone()
        price = str(record[0])

        self.root.ids.screen_mngr.current = screen
        self.root.ids.image_product.source = image
        #self.root.ids.image_product.size_hint_x = 0.9 + 0.9 + 0.9
        self.root.ids.details_product.text = lab
        self.root.ids.price_product.text = price
        self.select_product = lab
        self.price_product = price

    def change_product_phone(self, product_id, image, screen, size_x, size_y):

        sql_query_product = "select product from Products where id =%s"
        id_ = (product_id,)
        self.cursor_products.execute(sql_query_product, id_)
        record = self.cursor_products.fetchone()
        phone = str(record[0])

        sql_query_product = "select price from Products where id =%s"
        id_ = (product_id,)
        self.cursor_products.execute(sql_query_product, id_)
        record = self.cursor_products.fetchone()
        price = str(record[0])

        self.root.ids.screen_mngr.current = screen
        self.root.ids.image_product_phone.source = image
        self.root.ids.image_product_phone.size = size_x, size_y
        self.root.ids.details_product_phone.text = phone
        self.root.ids.price_product_phone.text = price
        self.select_product = phone
        self.price_product = price

    def plus_product_one(self):
        self.amount_product = self.amount_product + 1
        self.root.ids.amount.text = str(self.amount_product)

    def minus_product_one(self):
        if self.amount_product > 1:
            self.amount_product = self.amount_product - 1
        self.root.ids.amount.text = str(self.amount_product)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        print(instance, value, date_range)
        self.date = value
        print(self.date)

    # @staticmethod
    def on_cancel(self, instance, value):
        toast("Delivery time is missed")

    def show_date_picker(self):
        date_dialog = MDDatePicker(title_input="Delivery time")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def add_to_cart(self):

        my_dp_card = mysql.connector.connect(
            host="localhost",
            user="majidsaqr",
            password="135790521Mm@",
            database="EBay"
        )

        check_card = False

        cursor_add_cart = my_dp_card.cursor(dictionary=True)
        sql_select_query_add = "select * from Cart"
        cursor_add_cart.execute(sql_select_query_add)
        records_add_cart = cursor_add_cart.fetchall()

        for row in records_add_cart:
            product_cart_add = row["product"]
            price_cart_add = row["price"]
            if self.select_product == product_cart_add and self.price_product == price_cart_add:
                check_card = True

        if check_card:
            Snackbar(
                text="Already added",
                radius=[5, 15, 5, 15],
                snackbar_animation_dir="Left",
                snackbar_x="10dp",
                snackbar_y="10dp",
                bg_color=(0, 0, 1, 1),
                size_hint_x=(
                                    Window.width - (dp(10) * 2)
                            ) / Window.width
            ).open()
        else:
            if self.date != "":
                if self.amount_product > 0:
                    sql = "INSERT INTO Cart(name, email, phone, product, price, amount, delivery_time) VALUES (%s, " \
                          "%s, %s, %s, %s, %s, %s)"
                    val = (self.current_name, self.email, self.current_phone, self.select_product, self.price_product,
                           self.amount_product, self.date)
                    cursor_add_cart.execute(sql, val)
                    my_dp_card.commit()
                    Snackbar(
                        text="Add successfully",
                        radius=[5, 15, 5, 15],
                        snackbar_animation_dir="Left",
                        snackbar_x="10dp",
                        snackbar_y="10dp",
                        bg_color=(0, 0, 1, 1),
                        size_hint_x=(
                                            Window.width - (dp(10) * 2)
                                    ) / Window.width
                    ).open()
                    self.date = ""
                    self.amount_product = 0
                    self.root.ids.screen_mngr.current = "home1"
                else:
                    toast("Amount is missed")
            else:
                toast("Delivery time is missed")

    def show_products_cart(self):
        global cursor_show_cart
        try:
            sql_select_query = "select * from Cart"
            cursor_show_cart = self.my_dp.cursor(dictionary=True)

            cursor_show_cart.execute(sql_select_query)
            records_show_cart = cursor_show_cart.fetchall()

            list = []

            for row in records_show_cart:
                product_cart_show = row["product"]
                price_cart_show = row["price"]

                self.root.ids.add_fav_cart.add_widget(
                    TwoLineAvatarIconListItem(
                        IconLeftWidget(
                            icon="delete"
                        ),
                        text = product_cart_show,
                        secondary_text = price_cart_show,
                    )
                )

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.my_dp.is_connected():
                self.my_dp.close()
                cursor_show_cart.close()
                print("MySQL connection is closed")

if __name__ == '__main__':
    MainApp().run()
