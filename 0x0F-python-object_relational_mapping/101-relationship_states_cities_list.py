#!/usr/bin/python3
"""lists all State objects, and corresponding City objects, contained in
the database hbtn_0e_101_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ls = session.query(State).order_by(State.id)
    for st in ls:
        print("{}: {}".format(st.id, st.name))
        for c in st.cities:
            print("\t{}: {}".format(c.id, c.name))
    session.close()
