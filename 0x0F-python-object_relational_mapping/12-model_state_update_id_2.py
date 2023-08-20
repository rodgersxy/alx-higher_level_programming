#!/usr/bin/python3
"""
script that changes the name of a State object
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


def main():
    """
    Change the name of the State where id = 2 to New Mexico
    """
    if len(argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(
        State.id == 2).update({'name': 'New Mexico'})
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
