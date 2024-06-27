#!/usr/bin/python3
""" A script that deletes all State objects with a
    name containing the letter a from the database
    hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    items = query.filter(State.name.contains('a'))
    if items:
        for item in items:
            session.delete(item)

    session.commit()
    session.close()
