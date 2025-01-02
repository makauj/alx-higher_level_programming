#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    eng = create_engine(f"mysql+mysqldb://{usr}:{passwd}@localhost:3306/{db}")
    Session = sessionmaker(bind=eng)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
