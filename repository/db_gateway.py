import sqlalchemy as db
import sqlalchemy.orm

from repository.database import engine, Base, Product, User


class DataBaseGateway:
    session = sqlalchemy.orm.Session(bind=engine)

    def get_products(self) -> dict:
        connection = engine.connect()

        products = db.Table('product', Base.metadata, autoload=True, autoload_with=engine)
        query = db.select([products])
        result_query = connection.execute(query)

        return result_query.fetchall()

    def create(self, sku, name, price, brand):
        session = sqlalchemy.orm.Session(bind=engine)
        product = Product(sku=sku, name=name, price=price, brand=brand)
        session.add(product)
        session.commit()
        session.close()

    def delete(self, product_id):
        session = sqlalchemy.orm.Session(bind=engine)
        p = session.query(Product).get(product_id)
        session.delete(p)
        session.commit()
        session.close()

    def edit(self, product_id, sku, name, price, brand):
        session = sqlalchemy.orm.Session(bind=engine)

        p = session.query(Product).get(product_id)
        p.name = name
        p.sku = sku
        p.price = price
        p.brand = brand
        session.commit()
        session.close()

    def verifyPassword(self,username,password):
        session = sqlalchemy.orm.Session(bind=engine)

        u = session.query(User).filter_by(username=username).first()
        return u.verify_password(password)



