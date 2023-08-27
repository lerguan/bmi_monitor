# BMI_monitor

## Introduction

This is a Command Line Interface(CLI) app to create a BMI database for user to keep track their Body Mass Index(BMI) over the years. A new user can create their profile.Existing user can enter their current weight and height, find their most recent BMI and/or a list of BMI in an age range.

## Seed data to the datebase

All data is stored in the bmi_monitor.db file. For demostration purpose, fake data can be seeded to database using seed.py. First run `pipenv install && pipenv shell`. Then go to `lib/db` directory and run `python3 seed.py` to populate the database.

There are two tables in the database. One is `users` table, containing `first_name`, `last_name` and `dob` columns. The second is `bmis` table, containing `height`, `weight`, `bmi`, `user_id`, `age` columns. The `user_id` is the foreign key, which is refered to the primary key in `users` table.

## Instructions

### Start the app

First run `pipenv install && pipenv shell` if not in python 3 env. Then go to lib directory and run `python3 cli.py` to start the app.

When the app loads, it will ask user to input first name and last name. If name is in the datebase, it show main menu. Otherwise, it will ask if user wants to create profile.

### Main Menu

The main menu has three options, including `Input New height and weight`, `check BMI`, `Exit`. User can select each option for the submenus.

### Input New height and weight

In this submenu, user can input their recent height and weight to update their info. Their age and bmi will be automatically updated in the database.

### Check BMI submenu
