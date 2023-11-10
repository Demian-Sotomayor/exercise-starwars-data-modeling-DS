import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    favorites = relationship('Favorites', back_populates='user', uselist=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    population = Column(Integer, nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)    
    birth_year = Column(String(120), nullable=False)
    gender = Column(String(120), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
