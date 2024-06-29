#!/usr/bin/python3
"""A script that prints all city objects from
    the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    # session
    Session = sessionmaker(bind=engine)
    session = Session()
    # query
    results = session.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
