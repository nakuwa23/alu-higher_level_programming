#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first state by id
    first_state = session.query(State).order_by(State.id).first()

    # Display result or "Nothing" if table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
