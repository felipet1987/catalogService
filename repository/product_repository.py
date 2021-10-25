from repository.db_gateway import DataBaseGateway
from service.product_repository import ProductRepository


class ConcreteProductRepository(ProductRepository):
    product_gateway: DataBaseGateway

    def __init__(self, product_gateway: DataBaseGateway):
        self.product_gateway = product_gateway

    def get_list(self):
        products = self.product_gateway.get_products()
        return [{"id": p.id, "sku": p.sku,"price":p.price ,"name": p.name} for p in products]

    def create(self, sku, name, price, brand):
        self.product_gateway.create(sku, name, price, brand)

    def delete(self, product_id):
        self.product_gateway.delete(product_id)

    def edit(self, product_id, sku, name, price, brand):
        self.product_gateway.edit(product_id, sku, name, price, brand)
