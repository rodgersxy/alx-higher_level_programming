#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


def main():
    """
    main function
    list all State objects that contain letter 'a'
    """
    if len(argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id)

    for state in result:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    main()
