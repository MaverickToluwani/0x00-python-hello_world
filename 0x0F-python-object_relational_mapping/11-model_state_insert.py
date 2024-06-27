#!/usr/bin/python3
""" A Script that adds the state object "Louisiana"
    to the database "hbtn_0e_6_usa"
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    res = session.query(State.id).filter(State.name == "Louisiana").first()

    print(res[0])

    session.commit()

    session.close()
