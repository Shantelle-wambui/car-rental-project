from .crud import (
    get_customers,      #function to get all customers
    create_customer,    #function to create a new customer
    get_cars,           #function to get all cars
    get_available_cars, #function to get only available cars
    create_car,         #function to create a new car
    create_rental       #function to create a new rental
)
#first i import all database operation functions from crud.py
#this file makes the crud directory a python package
#it exports crud functionalities so they can be imported from other files