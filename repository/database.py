
import sqlalchemy
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///foo.db')
Base = declarative_base()



class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    sku = Column(String)
    name = Column(String)
    price = Column(Float)
    brand = Column(String)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(128))

    def hash_password(self, password):
        # self.password_hash = jwt.encode(
        #     {"password": password},
        #     "secret",
        #     algorithm='HS256'
        # )
        self.password_hash = password

    def verify_password(self, password):
        # return jwt.decode(self.password_hash, "secret") == password
        return self.password_hash == password


def init_db():
    Base.metadata.create_all(bind=engine)
    session = sqlalchemy.orm.Session(bind=engine)
    user = User()
    user.username = 'admin'
    user.hash_password("admin")
    session.add(user)
    session.commit()
    session.close()



