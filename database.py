from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
URL_DATABASE='mysql+pymysql://zohaib:1234567@localhost:3306/all-india'
engine =create_engine(URL_DATABASE)
try:
    connection=engine.connect()
    print("Connect to the database Successful")
    connection.close()
except Exception as e:
    print("error",e)    
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
