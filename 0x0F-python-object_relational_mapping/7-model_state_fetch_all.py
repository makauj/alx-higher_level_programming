#!/usr/bin/python3
"""
Script that lists all State objects from the
database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db = (f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    
    engine = create_engine(db)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{0}: {1}'.format(state.id, state.name))

    session.close()
