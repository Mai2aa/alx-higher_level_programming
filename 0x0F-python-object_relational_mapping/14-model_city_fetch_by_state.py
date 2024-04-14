#!/usr/bin/python3
"""cities in state"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name).filter(
                State.id == city.state_id).first()
        print("{}: ({}) {}".format(state_name[0], city.id, city.name))
