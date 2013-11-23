import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

import config

engine = create_engine(config.DATABASE_URL)
Session = sessionmaker()
Session.configure(bind = engine)

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key = True)
    title = Column(String(256))
    journal = Column(String(128))
    abstract = Column(Text)
    publisher = Column(String(128))
    issn = Column(String(9))
    year = Column(Integer)
    url = Column(String(256))

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key = True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    author = Column(String(128))

    article = relationship("Article", backref = backref("authors", order_by = id))

class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key = True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    keyword = Column(String(128))

    article = relationship("Article", backref = backref("keywords", order_by = id))

def setup_db():
    Base.metadata.create_all(engine)

