import json

from bs4 import BeautifulSoup
import requests


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://hello:1@localhost:5432/binance2")
# engine.connect()

url = 'https://www.binance.com/api/v3/ticker/price  '

def get_data(url):
    response = requests.get(url).text
    list_data = json.loads(response)
    return list_data    


Base = declarative_base()
class Deputy(Base):
    __tablename__= "pricesbinance"
    id = Column(Integer, primary_key = True)
    symbol = Column(String,)
    price = Column(String)

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


Deputy.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

data = get_data(url)
for i in data:
    session.add(Deputy(i["symbol"],i["price"]))
    session.commit()


from bs4 import BeautifulSoup
import requests


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://hello:1@localhost:5432/binance2")
# engine.connect()

url = 'https://www.binance.com/api/v3/ticker/price  '

def get_data(url):
    response = requests.get(url).text
    list_data = json.loads(response)
    return list_data    


Base = declarative_base()
class Deputy(Base):
    __tablename__= "pricesbinance"
    id = Column(Integer, primary_key = True)
    symbol = Column(String,)
    price = Column(String)

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


Deputy.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

data = get_data(url)
for i in data:
    session.add(Deputy(i["symbol"],i["price"]))
session.commit()





