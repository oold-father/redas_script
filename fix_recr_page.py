from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
import utils
import json

mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "redas"
mysql_name = "root"
mysql_password = "admin"

Base = declarative_base()


class Recr(Base):
    # 表的名字:
    __tablename__ = 'recr_page_storage'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    content = Column(String())
    hash = Column(String())
    spider_uuid = Column(String())


engine = create_engine(
    'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (mysql_name, mysql_password, mysql_host, mysql_port, mysql_db))

DBSession = sessionmaker(bind=engine)
session = DBSession()


def fix_address(contentJson):
    """
    """
    if "location" in contentJson:
        contentJson.update({"address": contentJson.get("location"), "city": contentJson.get("location")[:2]})
        contentJson.pop("location")


def main():
    id = 1
    flag = True
    while flag:
        print("正在进行第%s条记录"%id)
        data = None
        try:
            data = session.query(Recr).filter(Recr.id == id).one()
        except NoResultFound:
            break

        contentJson = json.loads(data.content, encoding="utf-8")

        # 将location字段更名为address
        fix_address(contentJson)

        # 将salary字段拆分
        contentJson.update(utils.split_salary(contentJson.get("salary")))

        # 将exp字段拆分
        contentJson.update(utils.split_exp(contentJson.get("exp")))

        # 将scale字段拆分
        contentJson.update(utils.split_scale(contentJson.get("scale")))

        # 拆分url
        contentJson["srcUrl"] = utils.remake_url(contentJson["srcUrl"])

        data.content = json.dumps(contentJson, ensure_ascii=False)
        data.hash = utils.strToHash(data.content)
        session.flush()
        id += 1

    session.commit()


if __name__ == "__main__":
    main()
    session.close()
