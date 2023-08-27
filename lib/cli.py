#!usr/bin/env python3
from helpers.banner import Banner
from simple_term_menu import TerminalMenu
from db.models import User, Bmi
import ipdb

banner=Banner()
user=User()
bmi=Bmi()
class Cli():

    def __init__(self):
        current_user = None

    def start(self):
        banner.welcome()
        print("Please enter your name")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        current_user = user.find_or_create_by(first_name, last_name)

        if current_user:
            self.current_user_menu(current_user, first_name, last_name)
            

    def current_user_menu(self, user, first_name, last_name):
        print(f"Welcome, {first_name} {last_name}!")
        options = ["Input New height and weight", "Check BMI", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "Input New height and weight":
            weight = float(input("Weight(lb): "))
            height = float(input("Height(ft) "))
            bmi.update_info(user, weight, height)

        elif options[menu_entry_index] == "Check BMI":
            pass

app = Cli()
app.start()