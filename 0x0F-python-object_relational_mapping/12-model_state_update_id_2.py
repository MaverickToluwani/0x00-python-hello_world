#!/usr/bin/python3
""" A script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    url = "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    state_name = query.filter(State.id == 2).update({"name": "New Mexico"})

    session.commit()

    session.close()
