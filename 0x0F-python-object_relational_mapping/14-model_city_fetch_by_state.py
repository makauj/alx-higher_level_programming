#!/usr/bin/python3
"""
Script to print all City objects in the database hbtn_0e_14_usa
sorted by cities.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get command-line arguments
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Create the engine and bind it to the Base
    eng = create_engine(f'mysql+mysqldb://{usr}:{passwd}@localhost:3306/{db}')

    # Create all tables in the database
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query the cities, join with the states, and sort by cities.id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
