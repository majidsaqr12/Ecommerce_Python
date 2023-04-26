from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget
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


class Confirm_Screen(Screen):
    pass


class MainApp(MDApp):
    
    ################ ( Variables User Sign Up )

    email = ""
    full_Name = ""
    password = ""
    confirm_password = ""

    ################ ( Variables Products )

    lab1 = ""
    lab2 = ""
    lab3 = ""
    lab3 = ""
    lab4 = ""
    lab5 = ""
    lab6 = ""

    phone1 = ""
    phone2 = ""
    phone3 = ""
    phone4 = ""
    phone5 = ""
    phone6 = ""

    ################ ( Variables prices Products )

    lab1_price = ""
    lab2_price = ""
    lab3_price = ""
    lab3_price = ""
    lab4_price = ""
    lab5_price = ""
    lab6_price = ""

    phone1_price = ""
    phone2_price = ""
    phone3_price = ""
    phone4_price = ""
    phone5_price = ""
    phone6_price = ""

    ################ ( Variables Confirm Product )

    fname = ""
    lname = ""
    phone = ""
    sphone = ""
    state = ""
    city = ""
    street = ""
    ddate = ""
    amount_product = 0
    select_product = ""
    price_product = ""

    ################

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

    # cursor.execute("CREATE DATABASE EBay")
    # cursor.execute("CREATE TABLE Orders_Buy(id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), price VARCHAR(255), Fname VARCHAR(255), Lname VARCHAR(255), phone VARCHAR(255), Sphone VARCHAR(255), state VARCHAR(255), city VARCHAR(255), street VARCHAR(255), Ddate VARCHAR(255), amount VARCHAR(255))")
    # cursor.execute("CREATE TABLE Cart(id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), price VARCHAR(255))")
    # cursor.execute("CREATE TABLE Cart_ID_Number(id INT AUTO_INCREMENT PRIMARY KEY, ID_Number VARCHAR(255))")


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
        sql_select_Query = "select * from DataUser"
        cursor2.execute(sql_select_Query)
        records = cursor2.fetchall()

        for row in records:
            e = row["email"]
            x = row["password"]
            if self.email == e and self.password == x:
                check_info = True         

        if self.root.ids.login_email.text != "":
            if self.root.ids.login_email.text.__contains__('@'):
                if self.root.ids.login_email.text.__contains__('.com'):
                        if self.password != "":
                            if check_info == True:
                                # self.root.ids.email_intent.text = "Email :  " + self.email
                                # self.root.ids.name_intent.text = "Name : " + self.full_Name
                                self.root.ids.screen_mngr.current = "home1"
                                self.root.ids.login_email.text = ""
                                self.root.ids.text_field.text = ""
                                self.root.ids.login_pass.text = ""
                                # kivymd.toast.kivytoast.kivytoast.toast("successfully", [], 10)
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

        check_email_founded = True

        cursor3 = self.my_dp.cursor(dictionary=True)
        sql_select_Query = "select * from DataUser"
        cursor3.execute(sql_select_Query)
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
                            if check_email_founded == True:
                                if self.password != "":
                                        if self.confirm_password == self.password:
                                            self.root.ids.screen_mngr.current = "home"
                                            self.root.ids.email_up.text = ""
                                            self.root.ids.full_name.text = ""
                                            self.root.ids.sign_up_pass.text = ""
                                            self.root.ids.sign_up_confirm_pass.text = ""
                                            toast('Registration completed successfully')
                                            sql = "INSERT INTO DataUser (name, email, password) VALUES (%s, %s, %s)"
                                            val = (self.full_Name, self.email, self.password)
                                            self.cursor.execute(sql, val)
                                            self.my_dp.commit()
                                            # self.my_dp.close()
                                        else:
                                            toast("passwords are not same")
                                else:
                                    toast("Password is missed")
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

    def sign_in_from_sign_up(self):
        self.root.ids.md_login.elevation = 4
        self.root.ids.screen_mngr.current = "home"

    def Add_success(self):
        toast("Add successfully")

    def skip(self):
        self.root.ids.screen_mngr.current = "home1"

    def change_product_lab1(self):

        sql_Query_product = "select product from Products where id =%s"
        id = (1,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab1 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (1,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab1_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap.jpg"
        self.root.ids.image_product.size_hint_x = 0.9 + 0.9 + 0.9
        self.root.ids.details_product.text = self.lab1
        self.root.ids.price_product.text = self.lab1_price
        self.select_product = self.lab1
        self.price_product = self.lab1_price

    def change_product_lab2(self):

        sql_Query_product = "select product from Products where id =%s"
        id = (2,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab2 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (2,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab2_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap2.png"
        self.root.ids.image_product.size_hint_x = 0.9 + 0.9
        self.root.ids.image_product.size_hint_y = 0.9 + 0.9
        self.root.ids.details_product.text = self.lab2
        self.root.ids.price_product.text = self.lab2_price
        self.select_product = self.lab2
        self.price_product = self.lab2_price

    def change_product_lab3(self):
        
        sql_Query_product = "select product from Products where id =%s"
        id = (3,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab3 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (3,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab3_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap3.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.6
        self.root.ids.details_product.text = self.lab3
        self.root.ids.price_product.text = self.lab3_price
        self.select_product = self.lab3
        self.price_product = self.lab3_price

    def change_product_lab4(self):

        sql_Query_product = "select product from Products where id =%s"
        id = (4,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab4 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (4,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab4_price = str(record[0])
        
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap4.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.9
        self.root.ids.image_product.radius = 36, 36, 0, 0
        self.root.ids.details_product.text = self.lab4
        self.root.ids.price_product.text = self.lab4_price
        self.select_product = self.lab4
        self.price_product = self.lab4_price

    def change_product_lab5(self):

        sql_Query_product = "select product from Products where id =%s"
        id = (5,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab5 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (5,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab5_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap5.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.6
        self.root.ids.image_product.radius = 36, 36, 0, 0
        self.root.ids.details_product.text = self.lab5
        self.root.ids.price_product.text = self.lab5_price
        self.select_product = self.lab5
        self.price_product = self.lab5_price

    def change_product_lab6(self):

        sql_Query_product = "select product from Products where id =%s"
        id = (6,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab6 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (6,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.lab6_price = str(record[0])
        
        self.root.ids.screen_mngr.current = "show_product"
        self.root.ids.image_product.source = "showlap/lap6.jpg"
        self.root.ids.image_product.size_hint_y = 0.9 + 0.9
        self.root.ids.image_product.radius = 36, 36, 0, 0
        self.root.ids.details_product.text = self.lab6
        self.root.ids.price_product.text = self.lab6_price
        self.select_product = self.lab6
        self.price_product = self.lab6_price

    def change_product_phone1(self):
        
        sql_Query_product = "select product from Products where id =%s"
        id = (7,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone1 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (7,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone1_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.9
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = self.phone1
        self.root.ids.price_product_phone.text = self.phone1_price
        self.select_product = self.phone1
        self.price_product = self.phone1_price

    def change_product_phone2(self):

        sql_Query_product = "select product from Products where id =%s"
        id = (8,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone2 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (8,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone2_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone1.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.9 + 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = self.phone2
        self.root.ids.price_product_phone.text = self.phone2_price
        self.select_product = self.phone2
        self.price_product = self.phone2_price

    def change_product_phone3(self):
        
        sql_Query_product = "select product from Products where id =%s"
        id = (9,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone3 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (9,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone3_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone2.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = self.phone3
        self.root.ids.price_product_phone.text = self.phone3_price
        self.select_product = self.phone3
        self.price_product = self.phone3_price

    def change_product_phone4(self):
        
        sql_Query_product = "select product from Products where id =%s"
        id = (10,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone4 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (10,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone4_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone3.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = self.phone4
        self.root.ids.price_product_phone.text = self.phone4_price
        self.select_product = self.phone4
        self.price_product = self.phone4_price

    def change_product_phone5(self):
        
        sql_Query_product = "select product from Products where id =%s"
        id = (11,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone5 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (11,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone5_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone4.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = self.phone5
        self.root.ids.price_product_phone.text = self.phone5_price
        self.select_product = self.phone5
        self.price_product = self.phone5_price

    def change_product_phone6(self):
        
        sql_Query_product = "select product from Products where id =%s"
        id = (12,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone6 = str(record[0])

        sql_Query_product = "select price from Products where id =%s"
        id = (12,)
        self.cursor_products.execute(sql_Query_product, id)
        record = self.cursor_products.fetchone()
        self.phone6_price = str(record[0])

        self.root.ids.screen_mngr.current = "show_product_phone"
        self.root.ids.image_product_phone.source = "showphone/phone5.jpg"
        self.root.ids.image_product_phone.size_hint_y = 0.9 + 0.5
        self.root.ids.image_product_phone.radius = 36, 36, 0, 0
        self.root.ids.details_product_phone.text = self.phone6
        self.root.ids.price_product_phone.text = self.phone6_price
        self.select_product = self.phone6
        self.price_product = self.phone6_price

    def plus_product_one(self):
        self.amount_product = self.amount_product + 1
        self.root.ids.amount.text = str(self.amount_product)

    def minus_product_one(self):
        if self.amount_product > 1:
            self.amount_product = self.amount_product - 1
        self.root.ids.amount.text = str(self.amount_product)

    def product_confirm_data(self):

        self.fname = self.root.ids.confirm_fname.text
        self.lname = self.root.ids.confirm_lname.text
        self.phone = self.root.ids.confirm_phone.text
        self.sphone = self.root.ids.confirm_sphone.text
        self.state = self.root.ids.confirm_state.text
        self.city = self.root.ids.confirm_city.text
        self.street = self.root.ids.confirm_street.text
        self.ddate = self.root.ids.confirm_Ddate.text

        if self.fname != "":
            if self.lname != "":
                if self.phone != "":
                        if self.sphone != "":
                                if self.state != "":
                                    if self.city != "":
                                        if self.street != "":
                                            if self.ddate != "":
                                                if self.amount_product != 0:
                                                    toast("The request has been registered successfully")
                                                    sql = "INSERT INTO Orders_Buy (product, price, Fname, Lname, phone, Sphone, state, city, street, Ddate, amount) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                                                    val = (self.select_product, self.price_product, self.fname, self.lname, self.phone, self.sphone, self.state, self.city, self.street, self.ddate, self.amount_product)
                                                    self.cursor.execute(sql, val)
                                                    self.my_dp.commit()
                                                    # self.my_dp.close()
                                                    self.root.ids.screen_mngr.current = "home1"
                                                    self.root.ids.confirm_fname.text = ""
                                                    self.root.ids.confirm_lname.text = ""
                                                    self.root.ids.confirm_phone.text = ""
                                                    self.root.ids.confirm_sphone.text = ""
                                                    self.root.ids.confirm_state.text = ""
                                                    self.root.ids.confirm_city.text = ""
                                                    self.root.ids.confirm_street.text = ""
                                                    self.root.ids.confirm_Ddate.text = ""
                                                    self.root.ids.amount.text = str(0)
                                                else:
                                                    toast("Amount is missed")
                                            else:
                                                toast("Delivery date is missed")
                                        else:
                                            toast("Street is missed")
                                    else:
                                        toast("City is missed")
                                else:
                                    toast("State is missed")
                        else:
                            toast("Second phone is missed")
                else:
                    toast("Phone is missed")
            else:
                toast("Last name missed")
        else:
            toast("First name missed")

    def add_to_cart(self):

        my_dp_card = mysql.connector.connect(
        host="localhost",
        user="majidsaqr",
        password="135790521Mm@",
        database="EBay"
        )

        check_card = False

        cursor_add_cart = my_dp_card.cursor(dictionary=True)
        sql_select_Query_add = "select * from Cart"
        cursor_add_cart.execute(sql_select_Query_add)
        records_add_cart = cursor_add_cart.fetchall()

        for row in records_add_cart:
            product_cart_add = row["product"]
            price_cart_add = row["price"]
            if self.select_product == product_cart_add and self.price_product == price_cart_add:
                check_card = True
            
        if check_card == True:
            toast("Already added")
        else:
            sql = "INSERT INTO Cart(product, price) VALUES (%s, %s)"
            val = (self.select_product, self.price_product)
            cursor_add_cart.execute(sql, val)
            my_dp_card.commit()
            toast("Add successfully")
            self.root.ids.screen_mngr.current = "home1"

    def hello (self):
        print("hello")

    def show_products_cart(self):
        try:
            sql_select_Query = "select * from Cart"
            cursor_show_cart = self.my_dp.cursor(dictionary=True)

            cursor_show_cart.execute(sql_select_Query)
            records_show_cart = cursor_show_cart.fetchall()

            for row in records_show_cart:
                product_cart_show = row["product"]
                price_cart_show = row["price"]
                self.root.ids.add_fav_cart.add_widget (
                    TwoLineAvatarIconListItem (   
                        IconLeftWidget(
                            icon="delete"
                        ),
                        text=product_cart_show,
                        secondary_text= price_cart_show,
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
