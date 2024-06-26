#!/usr/bin/python3
""" A script that prints the first
    State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    res = session.query(State.id, State.name).filter(State.id == 6).all()
    for i in res:
        print(f"{i[0]}: {i[1]}")

    session.close()
