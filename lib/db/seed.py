#!/usr/bin/env python3

from models import User, Bmi
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random
from datetime import date

if __name__ == '__main__':
    engine = create_engine("sqlite:///bmi_monitor.db")
    Session = sessionmaker(bind=engine)
    session = Session() 

    session.query(User).delete()
    session.query(Bmi).delete()

    fake = Faker()

    users = []
    for i in range(30):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            dob=fake.date_of_birth()
        )
        session.add(user)
        session.commit()
        users.append(user)

    bmis = []
    for user in users:    
        for i in range(random.randint(1, 10)):
            height = round(random.uniform(0.3, 9), 2)
            weight = round(random.uniform(3, 1000), 2)
            bmi_value = round(weight/(height**2), 2)
            age = date.today().year - user.dob.year
            bmi = Bmi(
                height = height,
                weight = weight,
                age = random.randint(0, age),
                bmi = bmi_value,
                user_id= user.id
            )

            bmis.append(bmi)
    
    session.bulk_save_objects(bmis)
    session.commit()
    session.close()