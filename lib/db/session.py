from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/bmi_monitor.db")
Session = sessionmaker(bind=engine)
session = Session()