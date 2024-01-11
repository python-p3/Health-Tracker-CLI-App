from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///models.db')
Session = sessionmaker(bind=engine)
session=Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(), unique=True, nullable=False)
    activities = relationship('Activity', back_populates='user')
    meals = relationship('Meal', back_populates='user')
    health_metrics = relationship('HealthMetric', back_populates='user')
    
    def __repr__(self):
        return f"ID:{self.id}, Name:{self.username}"
    
class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='activities')
    activity_type = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"Activity:{self.activity_type}, Duration: {self.duration_minutes}"
    
class Meal(Base):
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='meals')
    food_items = Column(String, nullable=False)
    nutritional_info = Column(String)
    
    def __repr__(self):
        return f"Food:{self.food_items}, Nutritional value: {self.nutritional_info}"
    
class HealthMetric(Base):
    __tablename__ = 'health_metrics'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='health_metrics')
    weight_kg = Column(Float)
    sleep_duration_hours = Column(Float)
    
    def __repr__(self):
        return f"Weight:{self.weight_kg}, Sleep Duration in Hours: {self.sleep_duration_hours}"