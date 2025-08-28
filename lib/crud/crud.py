from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models.models import Customer, Car, Rental
from datetime import datetime
#import database engine and session factory
#then i import model class customer

engine = create_engine("sqlite:///car_rental.db")
#i then create a connection to the database

Session = sessionmaker(bind=engine)
#create a session factory

def get_customers():
    session = Session()
    customers = session.query(Customer).all()
    session.close()
    return customers
#here i start by creating a new session
#query all customers from the database
#close the session to free up resources
#then return the list of customers


def create_customer(name, email, driver_license):
    session = Session()
    customer = Customer(name=name, email=email, driver_license=driver_license)
    session.add(customer)
    session.commit()
    session.close()
    return customer
#then i create a function to create new customer
#create a new session
#create a new customer object with the provided data
#add the new customer to the session
#commit the changes to save the customer to the database
#close the session
#then return the newly created customer


def get_cars():
    session = Session()
    cars = session.query(Car).all()
    session.close()
    return cars
#then i create a function to get all cars from the database
#query all cars from the databasr
#close the session 
#then return the list of cars

def get_available_cars():
    session = Session()
    cars = session.query(Car).filter(Car.available == True).all()
    session.close()
    return cars
#after, i create a function to get only available cars
#query cars where available=true


def create_car(model, brand, price_per_day):
    session = Session()
    car = Car(model=model, brand=brand, price_per_day=price_per_day)
    session.add(car)
    session.commit()
    session.close()
    return car
#here i create a function to create a new car
#create a new car object with the provided data
#add the new car to the session
#commit the changes to save the car to the database
#close the session
#and return the newly created car

def create_rental(customer_id, car_id, start_date, end_date):
    session = Session()
#then i create a function to create a new rental record    
    
    car = session.query(Car).filter(Car.id == car_id).first()
#first i find the car being rented
    
    if car:
        car.available = False
#if the car exists,mark it as unavailable
    
    rental = Rental(
        customer_id=customer_id,
        car_id=car_id,
        start_date=datetime.strptime(start_date, "%Y-%m-%d").date(),
        end_date=datetime.strptime(end_date, "%Y-%m-%d").date()
    )
#then i create a new rental object with the provided data
# convert string dates to proper date object


    session.add(rental)
    session.commit()
    session.close()
    return rental
#after i add the new rental to the session
#commit the changes to save the rental to the database
#close the session
#then return the newly created rental

