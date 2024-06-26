#!/usr/bin/python3

""" A script that lists all State objects from the
    database hbtn_0e_6_usa using the SQLAlchemy module
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create sessions
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    row = session.query(State.id, State.name).all()
    for r in row:
        print(f"{r[0]}: {r[1]}")
    session.close()
