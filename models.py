from sqlalchemy import Boolean,Column,Integer,String
from database import Base
class Vaccine(Base):
    __tablename__='vaccines'

    id=Column(Integer,primary_key=True,index=True)
    vaccinename=Column(String(50),unique=True)

class Brand(Base):
    __tablename__='brands'

    id=Column(Integer,primary_key=True,index=True)
    brandname=Column(String(50))
    purpose=Column(String(100))
    user_id=Column(Integer)