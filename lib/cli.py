#!usr/bin/env python3
from helpers.banner import Banner
from simple_term_menu import TerminalMenu
from db.models import User
import ipdb

banner=Banner()
user=User()

class Cli():

    def __init__(self):
        current_user = None

    def start(self):
        banner.welcome()
        print("Please enter your name")
        input_first_name = input("First Name: ")
        input_last_name = input("Last Name: ")
        current_user = user.find_or_create_by(input_first_name, input_last_name)

        if current_user:
            print(f"Welcome, {input_first_name} {input_last_name}!")
            options = ["Input New height and weight", "Check BMI", "Exit"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            
            if options[menu_entry_index] == "Input New height and weight":
                pass
            elif options[menu_entry_index] == "Check BMI":
                pass


app = Cli()
app.start()