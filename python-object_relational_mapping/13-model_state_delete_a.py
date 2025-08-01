#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # bind session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get and delete all states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # commit the changes
    session.commit()

    # close the session
    session.close()
