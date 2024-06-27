#!/usr/bin/python3
""" A script that lists all State objects that contain
    'a' from the database hbtn_0e_6_usa
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

    result = session.query(
            State.id, State.name
            ).filter(State.name.like('%a%')).order_by(State.id).all()
    for res in result:
        print(f"{res[0]}: {res[1]}")

    session.close()
