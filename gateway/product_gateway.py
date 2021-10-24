import sqlalchemy as db
import sqlalchemy.orm
from sqlalchemy import Column, Integer, String, create_engine, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    sku = Column(String)
    name = Column(String)
    price = Column(Float)
    brand = Column(String)


class ProductGateway:
    engine = create_engine('sqlite:///foo.db')
    session = sqlalchemy.orm.Session(bind=engine)

    def get_products(self) -> dict:
        connection = self.engine.connect()

        products = db.Table('product', Base.metadata, autoload=True, autoload_with=self.engine)
        query = db.select([products])
        result_query = connection.execute(query)

        return result_query.fetchall()

    def create(self, sku, name, price, brand):
        session = sqlalchemy.orm.Session(bind=self.engine)
        product = Product(sku=sku, name=name, price=price, brand=brand)
        session.add(product)
        session.commit()
        session.close()

    def delete(self, product_id):
        session = sqlalchemy.orm.Session(bind=self.engine)
        p = session.query(Product).get(product_id)
        session.delete(p)
        session.commit()
        session.close()

    def edit(self, product_id, sku, name, price, brand):
        session = sqlalchemy.orm.Session(bind=self.engine)

        p = session.query(Product).get(product_id)
        p.name = name
        p.sku = sku
        p.price = price
        p.brand = brand
        session.commit()
        session.close()

    def create_table(self):
        Base.metadata.create_all(self.engine)
