#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    eng = create_engine(f"mysql+mysqldb://{usr}:{passwd}@localhost:3306/{db}")
    Session = sessionmaker(bind=eng)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
