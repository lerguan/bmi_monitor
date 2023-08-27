from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from datetime import date
from .session import session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    
    bmis = relationship("Bmi", backref=backref("user"))

    @classmethod
    def find_or_create_by(cls, first_name, last_name):
        user = session.query(cls).filter(cls.first_name == first_name, cls.last_name == last_name).first()

        if user:
            return user
        else:
            print('invalid')


    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name})'
    
class Bmi(Base):
    __tablename__ = "bmis"

    id= Column(Integer, primary_key=True)
    height = Column(Float)
    weight = Column(Float)
    age = Column(Integer)
    bmi = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))


    @classmethod
    def update_info(cls, user, height, weight):
        bmi_value = round(weight/(height**2), 2)
        age = date.today().year - user.dob.year
        user_bmi = cls(
            height=height,
            weight=weight,
            age=age,
            bmi=bmi_value,
            user_id=user.id
        )
        session.add(user_bmi)
        session.commit()

    def __repr__(self):
        return f'Bmi(id={self.id}, ' + \
            f'height={self.height}, ' + \
            f'weight={self.weight}, ' + \
            f'date={self.date}, ' + \
            f'bmi={self.bmi})'