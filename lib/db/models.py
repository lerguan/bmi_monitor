from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    
    bmis = relationship("Bmi", backref=backref("user"))

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

    def __repr__(self):
        return f'Bmi(id={self.id}, ' + \
            f'height={self.height}, ' + \
            f'weight={self.weight}, ' + \
            f'date={self.date}, ' + \
            f'bmi={self.bmi})'