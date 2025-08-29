from sqlalchemy import create_engine, inspect
from db.models.models import Base


def debug_database():
#then i create function to display database structure
    engine = create_engine("sqlite:///car_rental.db")
#connect to the database 

    inspector = inspect(engine)
 #create an inspector to examine the database    
    
    tables = inspector.get_table_names()
#get all table names in the database
    
    print("Database Tables:")
#display each table and its columns

    for table in tables:
        print(f"\nTable: {table}")
#get all columns in this table

        for column in inspector.get_columns(table):
#get all columns in this table 
           
         print(f"  {column['name']} ({column['type']})")
#displays column name and type

if __name__ == "__main__":
    debug_database()
#runs the debug function if this script is executed directly