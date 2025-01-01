#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}')
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).order_by(State.id).all()
    
    for state in states:
        print(f'{state.id}: {state.name}')
    
    session.close()