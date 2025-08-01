#!/usr/bin/python3
"""Updates the name of a State object with id = 2 to 'New Mexico'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State with id=2
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
