#!usr/bin/env python3
from helpers.banner import Banner
from simple_term_menu import TerminalMenu
from db.models import User, Bmi
from datetime import date
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
        current_user = user.find(first_name, last_name)

        if current_user:
            self.current_user_menu(current_user)
        else:
            print("User is not found! Do you want to create new user profile?")
            
            options = ["Yes", "No"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            
            if options[menu_entry_index] == "Yes":
                print(f"Welcom, {first_name} {last_name}!")
                dob_input = input("Please enter your date of birth (yyyy-mm-dd): ")
                date_format = "%Y-%m-%d"
                res = True
                try:
                    res = bool(date.strptime(dob_input, date_format))
                except ValueError:
                    res = False
                if res:
                    dob = date.strftime(dob_input, date_format)
                    user.create_user(first_name, last_name, dob)
                else:
                    print("Please enter valid date of birth")
            
            

    def current_user_menu(self, user):
        print(f"Welcome, {user.first_name} {user.last_name}!")
        options = ["Input New height and weight", "Check BMI", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "Input New height and weight":
            weight = float(input("Weight(lb): "))
            height = float(input("Height(ft) "))
            bmi.update_info(user, weight, height)
            self.current_user_menu(user)

        elif options[menu_entry_index] == "Check BMI":
            pass

app = Cli()
app.start()