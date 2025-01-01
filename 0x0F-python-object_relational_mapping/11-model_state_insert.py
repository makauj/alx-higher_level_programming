#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    eng = create_engine(f'mysql+mysqldb://{usr}:{passwd}@localhost:3306/{db}')
    Base.metadata.create_all(eng)

    Session = sessionmaker(bind=eng)
    session = Session()
    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()

    print(add_state.id)

    session.close()    
