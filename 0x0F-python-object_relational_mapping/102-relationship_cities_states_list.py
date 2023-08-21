#!/usr/bin/python3
"""
a script that lists all City objects from the database
hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    if len(argv) != 4:
        return

    """Create an engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    """ Create the tables defined by Base in the database"""
    Base.metadata.create_all(engine)

    """ a session for querying database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(state.id, state.name, state.state.name))

    session.close()


if __name__ == "__main__":
    main()
