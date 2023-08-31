from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session 
app=FastAPI()
models.Base.metadata.create_all(bind=engine)
class BrandBase(BaseModel):
   brandname:str
   purpose:str
   user_id:int
class VaccineBase(BaseModel):
   vaccinename:str
def get_db():
   db=SessionLocal()
   try:
       yield db
   finally:
      db.close()
db_dependency=Annotated[Session,Depends(get_db)]   
@app.post("/vaccine/",status_code=status.HTTP_201_CREATED)
async def create_vaccine(vaccine:VaccineBase,db:Session=Depends(get_db)):
   db_vaccine=models.Vaccine(**vaccine.dict())
   db.add(db_vaccine)
   db.commit() 

@app.get("/vaccine/",status_code=status.HTTP_200_OK)
async def read_vaccine(db:db_dependency):
   vaccine=db.query(models.Vaccine).all()
   if vaccine is None:
      raise HTTPException(status_code=404,detail='vaccine not found')
   return vaccine
@app.post("/brand/",status_code=status.HTTP_201_CREATED)
async def create_brand(brand:BrandBase,db:db_dependency):
   db_brand=models.Brand(**brand.dict())
   db.add(db_brand)
   db.commit() 
@app.get("/brand/",status_code=status.HTTP_200_OK)
async def read_brand(db:db_dependency):
  brand=db.query(models.Brand).all()
  if brand is None:
      raise HTTPException(status_code=404,detail='Brand not found')
  return brand

@app.put("/vaccine/",status_code=status.HTTP_200_OK)
async def update_vaccine(user_id:int,db:db_dependency):
   vaccine=db.query(models.Vaccine).filter(models.Vaccine.id==user_id).first()
   if vaccine is None:
      raise HTTPException(status_code=404,detail='Vaccine not found')
   return vaccine
@app.put("/brand/",status_code=status.HTTP_200_OK)
async def update_brand(post_id:int,db:db_dependency):
  brand=db.query(models.Brand).filter(models.Brand.id==post_id).first()
  if brand is None:
      raise HTTPException(status_code=404,detail='Brand not found')
  return brand

@app.delete("/vaccine/",status_code=status.HTTP_200_OK)
async def delete_vaccine(user_id:int,db:db_dependency):
   db_vaccine=db.query(models.Vaccine).filter(models.Vaccine.id==user_id).first()
   if db_vaccine is None:
      raise HTTPException(status_code=404,detail='Vaccine not found')
   db.delete(db_vaccine) 
   db.commit()

@app.delete("/brand/",status_code=status.HTTP_200_OK)
async def delete_brand(post_id:int,db:db_dependency):
   db_brand=db.query(models.Brand).filter(models.Brand.id==post_id).first()
   if db_brand is None:
      raise HTTPException(status_code=404,detail='Brand not found')
   db.delete(db_brand) 
   db.commit()
