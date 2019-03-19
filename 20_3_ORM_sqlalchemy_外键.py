# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import INTEGER
from sqlalchemy.dialects.mysql import LONGTEXT


# 数据库配置
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '3306'
NAME = 'wechat_article_spider'

# 创建对象的基类:
Base = declarative_base()


# 定义 wechat_article_data 对象:
class WechatArticleData(Base):
    # 表的名字:
    __tablename__ = 'wechat_article_table'

    # 表的结构:
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(200))
    is_original = Column(String(4))
    publisher_author_name = Column(String(30))
    publisher = Column(String(30))
    publish_time = Column(String(30))
    text = Column(LONGTEXT)
    # crawl_time = Column(INTEGER, nullable=False)
    parser_time = Column(INTEGER, nullable=False)
    # url = Column(String(300), nullable=False)
    url = Column(String(300), unique=True, nullable=False)  # 要用做外键的要求unique=True,
    html_data_foreign_key = relationship('WechatArticleHtmlData', backref='article_of_html')  # 一
    source_type = Column(String(20))


class WechatArticleHtmlData(Base):
    # 表的名字:
    __tablename__ = 'wechat_article_html_table'

    # 表的结构:
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    url = Column(String(300), ForeignKey('wechat_article_table.url'))
    html_str = Column(LONGTEXT)


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(USER, PASSWORD, HOST, PORT, NAME))
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 创建数据表
Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 正查
articles = session.query(WechatArticleData).filter_by().all()
for article in articles:
    html_data_foreign_key = article.html_data_foreign_key  # 多
    for html_data in html_data_foreign_key:
        print(html_data.url)
        print(html_data.html_str)

# 反查
html_datas = session.query(WechatArticleHtmlData).filter_by().all()
for html_data in html_datas:
    article = html_data.article_of_html  # 一
    print(article.is_original)

# 关闭Session:
session.close()
