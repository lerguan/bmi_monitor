# BMI_monitor

## Introduction

This is a Command Line Interface(CLI) app to create a BMI database for user to keep track their Body Mass Index(BMI) over the years. A new user can create their profile.Existing user can enter their current weight and height, find their most recent BMI and/or a list of BMI in an age range.

## Seed data to the datebase

All data is stored in the bmi_monitor.db file. For demostration purpose, fake data can be seeded to database using seed.py. First run `pipenv install && pipenv shell`. Then go to `lib/db` directory and run `python3 seed.py` to populate the database.

## Instructions

### Start the app

First run `pipenv install && pipenv shell` if not in python 3 env. Then go to lib directory and run `python3 cli.py` to start the app.

When the app loads, the page shows the existing collection of games and the number of titles in the collection from each period of time

### Add new game to collection

On the bottom of the page, there is form where you can input game information and click create button to store the new game information to the collection. Meanwhile, the flyer image of the new added game shows up in its corresponding release date time peroid. The total number of game titles also updates on the top time peroid tab.

### Show specific game information

When move the mouse to a specific game flyer image and click that image, the detail information including title, release date, gameplay image and number of player allowed shows up on the center of the screen while the rest of the page is faded.

### Remove specific game from the collection

When click the `Remove Game` button under each game flyer image, the game is deleted from the page as well as from the server. Meanwhile, the total number of title updates accordingly.

### Credit

The game information is from `wikipedia.org`, `arcade-museum.com`, `culturedvultures.com` and `segakore.fr`
