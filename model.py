from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Picture(Base):
	__tablename__= 'Pictures'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	picture_link = Column(String)