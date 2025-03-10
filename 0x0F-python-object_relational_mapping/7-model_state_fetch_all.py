#!/usr/bin/python3
"""
Script that lists all State objects from the
database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
        @localhost:3306/{argv[3]}')
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
