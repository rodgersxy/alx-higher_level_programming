#!/usr/bin/python3
"""
a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


def main():
    """
    prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
    """
    if len(argv) != 5:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    key = 0
    for state in session.query(State):
        if argv[4] == state.name:
            print("{}".format(state.id))
            key = 1
    if key == 0:
        print("Not found")
    session.close()


if __name__ == "__main__":
    main()
