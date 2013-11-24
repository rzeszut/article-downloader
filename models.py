from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

import config

engine = create_engine(config.DATABASE_URL)
Session = sessionmaker()
Session.configure(bind = engine)

Base = declarative_base()

def setup_db():
    Base.metadata.create_all(engine)

#
# Articles
#

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
    source = Column(String(32))

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

#
# Patents
#

class Patent(Base):
    __tablename__ = 'patents'

    id = Column(Integer, primary_key = True)
    name = Column(String(256))
    date = Column(Date)
    application_number = Column(String(64))
    priority_number = Column(String(64))
    abstract = Column(Text)

class Inventor(Base):
    __tablename__ = 'inventors'

    id = Column(Integer, primary_key = True)
    patent_id = Column(Integer, ForeignKey('patents.id'))
    inventor = Column(String(128))

    patent = relationship("Patent", backref = backref("inventors", order_by = id))

class Applicant(Base):
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key = True)
    patent_id = Column(Integer, ForeignKey('patents.id'))
    applicant = Column(String(128))

    patent = relationship("Patent", backref = backref("applicants", order_by = id))

class InternationalClassification(Base):
    __tablename__ = 'international_classifications'

    id = Column(Integer, primary_key = True)
    patent_id = Column(Integer, ForeignKey('patents.id'))
    international_classification = Column(String(64))

    patent = relationship("Patent", backref = backref("international_classifications", order_by = id))

class CooperativeClassification(Base):
    __tablename__ = 'cooperative_classifications'

    id = Column(Integer, primary_key = True)
    patent_id = Column(Integer, ForeignKey('patents.id'))
    cooperative_classification = Column(String(64))

    patent = relationship("Patent", backref = backref("cooperative_classifications", order_by = id))

