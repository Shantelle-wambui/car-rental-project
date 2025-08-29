from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Customer, Car

#import database engine and model definitions

engine = create_engine("sqlite:///car_rental.db")
#then i create a connection to sqlite database
#the database will be stored in a file called car_rental.db

Base.metadata.create_all(engine)
#this creates  the customers, cars and rental tables in the database

Session = sessionmaker(bind=engine)
#creates a session factory to interact with the database

session = Session()
#creates a new session

customers = [
    Customer(name="Shantelle kish", email="shantellek@example.com", driver_license="DL12345"),
    Customer(name="Janey Smith", email="janey@example.com", driver_license="DL67890")
]
#then i create a sample customer data to populate the database


cars = [
    Car(model="Civic", brand="Honda", available=True, price_per_day=45),
    Car(model="Corolla", brand="Toyota", available=True, price_per_day=40),
    Car(model="F-150", brand="Ford", available=True, price_per_day=80)
]
#then i create a sample car data to populate the database

session.add_all(customers)
session.add_all(cars)
#add all sample data to the session

session.commit()
#then commit the changes to the database
#this saves all the data permanently

print("Database seeded with sample data!")
session.close()