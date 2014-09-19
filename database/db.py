#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: db.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-09
#      History: 
#=============================================================================


from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, Text, TEXT, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_CONNECT_STRING = 'mysql+mysqldb://jm_waf:jumei_system@192.168.1.19/jm_waf?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=False)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(engine)
#
# def drop_db():
#     BaseModel.metadata.drop_all(engine)


class Hack(BaseModel):
    __tablename__ = 'jm_hacker'

    id = Column(Integer, primary_key=True)
    ip = Column(CHAR(60))
    hack_city = Column(CHAR(40))
    hack_addr = Column(CHAR(40))
    url = Column(TEXT())
    host = Column(CHAR(80))
    acl = Column(TEXT(80))
    src_time = Column(DATETIME(20))
    method = Column(CHAR(10))
    headers = Column(TEXT())
    user_agent = Column(TEXT(80))
    cookie = Column(TEXT(80))
    post_data = Column(TEXT())

if __name__ == '__main__':
    init_db()