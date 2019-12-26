#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 下午5:18
# @Author  : yinxin
# @File    : fix_position
# @Software: PyCharm


from sqlalchemy import Column, String, create_engine, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
import utils


mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "redas"
mysql_name = "root"
mysql_password = "admin"

Base = declarative_base()


class Position(Base):
    # 表的名字:
    __tablename__ = 'position'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    _describe = Column(String())
    edu = Column(String())
    exp = Column(String())
    address = Column(String())
    position = Column(String())
    publish_time = Column(Date())
    salary = Column(String())
    src_name = Column(String())
    src_pos_id = Column(String())
    src_url = Column(String())
    city = Column(String())
    kind = Column(String())
    exp_max = Column(Integer())
    exp_min = Column(Integer())
    salary_max = Column(Integer())
    salary_min = Column(Integer())
    several = Column(Integer())



engine = create_engine(
    'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (mysql_name, mysql_password, mysql_host, mysql_port, mysql_db))

DBSession = sessionmaker(bind=engine)
session = DBSession()


def main():
    id = 0
    while id <44475:
        id += 1
        print("正在进行第%s条记录" % id)
        data = None
        try:
            data = session.query(Position).filter(Position.id == id).one()
        except NoResultFound:
            print("NoResultFound")
            continue


        salary = utils.split_salary(data.salary)
        data.salary_max = salary.get("salaryMax")
        data.salary_min = salary.get("salaryMin")
        data.several  = salary.get("several")

        exp = utils.split_exp(data.exp)
        data.exp_max= exp.get("expMax")
        data.exp_min = exp.get("expMin")

        session.flush()
    session.commit()


if __name__ == '__main__':
    main()