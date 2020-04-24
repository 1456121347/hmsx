# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, MetaData, String
from sqlalchemy.schema import FetchedValue
# from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from application import db

# Base = declarative_base()
# metadata = Base.metadata



class User(db.Model):
    __tablename__ = 'user'

    uid = Column(BigInteger, primary_key=True, info='??id')
    nickname = Column(String(100), nullable=False, server_default=FetchedValue(), info='????')
    mobile = Column(String(20), nullable=False, server_default=FetchedValue(), info='????')
    email = Column(String(100), nullable=False, server_default=FetchedValue(), info='????')
    sex = Column(Integer, nullable=False, server_default=FetchedValue(), info='1:? 2:? 0:????')
    avatar = Column(String(64), nullable=False, server_default=FetchedValue(), info='??')
    login_name = Column(String(20), nullable=False, unique=True, server_default=FetchedValue(), info='?????')
    login_pwd = Column(String(32), nullable=False, server_default=FetchedValue(), info='????')
    login_salt = Column(String(32), nullable=False, server_default=FetchedValue(), info='?????????')
    status = Column(Integer, nullable=False, server_default=FetchedValue(), info='1:?? 0:??')
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue(), info='????????')
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue(), info='????')
