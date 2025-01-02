#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an
argument from the database hbtn_0e_6_usa
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

    state = session.query(State).filter_by(state_name=sys.argv[4]).first()

    if state is not None:
        print(str(state.id))
    else:
        print("Not found")

    session.close()
