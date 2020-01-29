from model import Base, Picture

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread':False},)
Base.metadata.create_all(engine)
DBSession = scoped_session(sessionmaker(bind=engine,autoflush=False))
session = DBSession()

def add_picture(name, description, picture_link):

	product_object = Picture(
		name = name,
		description = description,
		picture_link = picture_link)
	session.add(product_object)
	session.commit()

def edit_picture(id, name, description, picture_link):

	product_object = session.query(
		Picture).filter_by(
		id=id).first()
	product_object.name = name
	product_object.description = description
	product_object.picture_link = picture_link
	session.add(product_object)
	session.commit()

def delete_picture(id):
	session.query(Picture).filter_by(
		id = id).delete()
	session.commit()

def return_all_pictures():
	pictures = session.query(Picture).all()
	return pictures

def query_by_id(their_id):
	pictures = session.query(Picture).filter_by(id = their_id).delete()
	session.commit()

query_by_id(1)