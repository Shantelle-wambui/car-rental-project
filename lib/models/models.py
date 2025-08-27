from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

#first i import necessary SQLAlchemy components

Base = declarative_base()
#then i create a base class for my database models
#here all my model classes will inherit from this base class


class Customer(Base): 
    #i start of by difining the customer model(table)

    __tablename__ = "customers"
    #then i set the table name in the database
    
    id = Column(Integer, primary_key=True) #this acts as a unque identifier for each customer
    name = Column(String)   #customer's full name
    email = Column(String)   #customer's email address
    driver_license = Column(String)  #customer's driver license number


class Car(Base):
    #then i define the car model(table)

    __tablename__ = "cars"
    #set the table name in the database

    id = Column(Integer, primary_key=True)  #unique identifier for each car
    model = Column(String)  #car model
    brand = Column(String)  #car brand
    available = Column(Boolean, default=True)  # whether the car is available for rent
    price_per_day = Column(Integer)  #rental price per day

class Rental(Base):
    #then i define the rental model(table) to track car rentals

    __tablename__ = "rentals"
    #set the table name in the database

    id = Column(Integer, primary_key=True)  #unique identifier for each rental
    customer_id = Column(Integer, ForeignKey("customers.id"))   #links to customer
    car_id = Column(Integer, ForeignKey("cars.id"))  #links to car
    start_date = Column(Date)   #rental start date
    end_date = Column(Date)   #rental end date