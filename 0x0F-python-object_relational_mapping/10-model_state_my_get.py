#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an
argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}\
        @localhost:3306/{}'.format(argv[1], argv[2], argv[3]),)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(state_name=argv[4]).first()

    if state is not None:
        print(str(state.id))
    else:
        print("Not found")

    session.close()
