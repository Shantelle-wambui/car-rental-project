from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models.models import Customer
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
#commit the changes to savee the customer to the database
#close the session
#then return the newly created customer
