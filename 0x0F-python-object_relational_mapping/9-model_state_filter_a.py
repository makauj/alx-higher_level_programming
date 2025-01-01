#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{usr}:{passwd}@localhost/{db}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    s = '%a%'
    row = session.query(State).filter(State.name.like(s)).order_by(State.id)

    for state in row:
        print(f'{state.id}: {state.name}')

    session.close()
