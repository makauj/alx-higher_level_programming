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
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    eng = create_engine(f'mysql+mysqldb://{usr}:{passwd}@localhost:3306/{db}')

    Base.metadata.create_all(eng)

    Session = sessionmaker(bind=eng)
    session = Session()

    # Query the cities, join with the states, and sort by cities.id
    cities = session.query(City, State).join(State).all()

    # Print the results in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()

    # Close the session
    session.close()
