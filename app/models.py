from sqlalchemy import Column, Integer, TEXT, String, TIMESTAMP
from app import Base
from app import engine
from datetime import datetime


class Stocks(Base):
    __tablename__ = "stockbot_stocks"
    __bind_key__ = 'public'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    stockname = Column(String(30))
    subreddit = Column(String(30))
    count = Column(Integer)
    first_seen = Column(TIMESTAMP(), default=datetime.utcnow())
    last_seen = Column(TIMESTAMP())
    reddit_post_id = Column(String(10))


class StocksCount(Base):
    __tablename__ = "stockbot_stocks_count"
    __bind_key__ = 'public'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    stockname = Column(String(30))
    count = Column(Integer)
    subreddit = Column(String(30))


Base.metadata.create_all(engine)
