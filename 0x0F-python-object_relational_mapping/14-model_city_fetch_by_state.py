#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City, Base
from sys import argv


def main():
    if len(argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
