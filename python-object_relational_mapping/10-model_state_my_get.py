#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get credentials and search name from command-line arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create engine for database connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the state by name (safe from SQL injection)
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
