#!usr/bin/env python3
from helpers.banner import Banner
from simple_term_menu import TerminalMenu
import ipdb

banner=Banner()
def start():
    banner.welcome()
    print("Please enter your Name to get start")
    input_first_name = input("First Name: ")
    input_last_name = input("Last Name: ")

    handle_name_input(input_first_name, input_last_name)
    ipdb.set_trace()

    options = [""]

    def handle_name_input(first_name, last_name):
        pass
start()