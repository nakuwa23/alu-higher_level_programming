#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete states containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close session
    session.close()
