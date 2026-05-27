from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://ruvay_user:WL2WrZihzcWnVt4H8O9K2m0G2yXZEtzU@dpg-d5e2356uk2gs739an4j0-a.virginia-postgres.render.com/ruvay"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()