#!usr/bin/env python3
from helpers.banner import Banner
from simple_term_menu import TerminalMenu
from db.models import User, Bmi
from datetime import datetime
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
        first_name_input = input("First Name: ")
        last_name_input = input("Last Name: ")
        self.handle_current_user(first_name_input, last_name_input)

    def handle_current_user(self, first_name, last_name):   
        current_user = user.find(first_name, last_name)

        if current_user:
            self.current_user_menu(current_user)
        else:
            print("User is not found! Do you want to create new user profile?")
            
            options = ["Yes", "No"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            
            if options[menu_entry_index] == "Yes":
                print(f"Welcome, {first_name} {last_name}!")
                self.handle_dob_input(first_name, last_name)
                self.handle_current_user(first_name, last_name)

    def handle_dob_input(self, first_name, last_name):
        dob_input = input("Please enter your date of birth (yyyy-mm-dd): ")
        date_format = "%Y-%m-%d"
        res = True
        try:
            res = bool(datetime.strptime(dob_input, date_format))
        except ValueError:
            res = False
        if res:
            dob = datetime.strptime(dob_input, date_format)
            user.create(first_name, last_name, dob)
            self.handle_current_user(first_name, last_name)

        else:
            print("Please enter valid date of birth")
            self.handle_dob_input(first_name, last_name)

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
            options = ["Most Recent BMI", "List of BMI in time period", "Back", "Exit"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()

            if options[menu_entry_index] == "Most Recent BMI":
                self.handle_most_recent_bmi(user)
                self.back_to_main_menu(user)

            elif options[menu_entry_index] == "List of BMI in time period":
                self.handle_bmi_list()
                self.back_to_main_menu(user)
            elif options[menu_entry_index] == "Back":
                self.current_user_menu(user)

    def handle_most_recent_bmi(self, user):
        bmi_value = bmi.last_bmi(user)
        print(f"Your most recent BMI is: {bmi_value}")

    def back_to_main_menu(self, user):
        options = ["Back to main menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options:
            self.current_user_menu(user)

app = Cli()
app.start()