from repository.product_repository import ConcreteProductRepository

from rest.product_request import ProductRequest


class ProductService:
    product_repository: ConcreteProductRepository

    def __init__(self, product_repository: ConcreteProductRepository):
        self.product_repository = product_repository

    def get_list(self):
        return self.product_repository.get_list()

    def create(self, product: ProductRequest):
        self.product_repository.create(
            product.sku,
            product.name,
            product.price,
            product.brand
        )

    def delete(self, product_id):
        self.product_repository.delete(product_id)

    def edit(self, product_id, product):
        self.product_repository.edit(
            product_id,
            product.sku,
            product.name,
            product.price,
            product.brand
        )
