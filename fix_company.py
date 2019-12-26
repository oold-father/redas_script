#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 下午4:51
# @Author  : yinxin
# @File    : fix_company
# @Software: PyCharm

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
import utils


mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "redas"
mysql_name = "root"
mysql_password = "geek"

Base = declarative_base()


class Company(Base):
    # 表的名字:
    __tablename__ = 'company'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    main_page = Column(String())
    name = Column(String())
    scale = Column(String())
    scale_right = Column(Integer())
    scale_left = Column(Integer())


engine = create_engine(
    'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (mysql_name, mysql_password, mysql_host, mysql_port, mysql_db))

DBSession = sessionmaker(bind=engine)
session = DBSession()


def main():
    id = 0
    while id < 19833:
        id += 1
        print("正在进行第%s条记录" % id)
        data = None
        try:
            data = session.query(Company).filter(Company.id == id).one()
        except NoResultFound:
            print("NoResultFound")
            continue


        data.main_page = data.main_page if not data.main_page == "http://" else None

        result = utils.split_scale(data.scale)
        data.scale_right = result.get("scaleRight")
        data.scale_left = result.get("scaleLeft")

        session.flush()

    session.commit()


if __name__ == '__main__':
    main()