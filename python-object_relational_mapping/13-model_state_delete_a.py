#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Credentials and database name from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states where name contains 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each matched state
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
