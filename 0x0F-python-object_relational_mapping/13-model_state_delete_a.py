#!/usr/bin/python3
""" delete all states that has the letter a in it"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_state = session.query(State).filter(State.name.like("%a%"))
    if delete_state:
        for state in delete_state:
            session.delete(state)
        session.commit()
