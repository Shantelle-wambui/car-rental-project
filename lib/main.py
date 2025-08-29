from crud import get_available_cars, get_customers, create_customer, create_rental
#first i import database operation functions

def show_available_cars():
#then i create a function to display all available cars
    
    cars = get_available_cars()
#then i get the list of available cars from the database  
    
    if not cars:
        print("No cars available at the moment.")
        return
#then i check if there are any available cars
    # Display each available car with its details
    print("\nAvailable Cars:")
    for car in cars:
        print(f"{car.id}. {car.brand} {car.model} - ${car.price_per_day}/day")
#displays each available car with its details

def register_customer():
    print("\nRegister New Customer")
#then i create a function to register a new customer
    
    name = input("Name: ")
    email = input("Email: ")
    license = input("Driver license: ")
#here i get customer information from user input    
    
    create_customer(name, email, license)
    
    # Confirm successful registration
    print("Customer registered successfully!")
#here i confirm successful registration

def rent_car():
    print("\nRent a Car")
#then i create a function to process a car rental
    
    customers = get_customers()
#get all customers from the database 
 
    if not customers:
        print("No customers found. Please register a customer first.")
        return
#then i check if there are any registered customers      
   
    print("Select a customer:")
    for customer in customers:
        print(f"{customer.id}. {customer.name}")
    
    try:

        customer_id = int(input("Customer ID: "))
#check if there are any registered customers    
    
        cars = get_available_cars()
 #get available cars for rental   
      
        if not cars:
            print("No cars available for rental.")
            return
#then i check if there are any available cars            

        print("Available cars:")
        for car in cars:
            print(f"{car.id}. {car.brand} {car.model}")
    #display available cars for selection        
       
        car_id = int(input("Car ID: "))
 #get car selection from user 

        start_date = input("Start date (YYYY-MM-DD): ")
        end_date = input("End date (YYYY-MM-DD): ")
 #get rental period from user 
       
        create_rental(customer_id, car_id, start_date, end_date)
 #then i create the rental record in the database      
        
        print("Car rented successfully!")
#then i confirm successful rental
     
    
    except ValueError:
        print("Please enter valid numbers for IDs.")
#this handles invalid input errors        

    except Exception as e:
        print(f"Error: {e}")
#handle any other errors

def main():
    
    print("Welcome to Car Rental Management System!")
#displays welcome message    
    
    while True:
       
        print("\nMain Menu:")
        print("1. View available cars")
        print("2. Register customer")
        print("3. Rent car")
        print("4. Exit")
 #displays menu options
      
        choice = input("Choose option (1-4): ")
#get user choice        
        
        if choice == "1":
            show_available_cars()
        elif choice == "2":
            register_customer()
        elif choice == "3":
            rent_car()
        elif choice == "4":
            print("Thank you for using Car Rental Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
#handle invalid menu choices

if __name__ == "__main__":
    main()
#this ensures the main function runs only when the script is executed directly