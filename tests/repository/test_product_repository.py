from gateway.product_gateway import ProductGateway, Product
from repository.product_repository import ConcreteProductRepository


def test_get(monkeypatch):
    product = Product()
    product.sku = "sku"
    product.name = "test"
    product.price = 23.2
    product.brand = "brand"
    product.id = 1

    def mock_get(*args, **kwargs):
        return [product]

    monkeypatch.setattr(ProductGateway, "get_products", mock_get)
    gateway = ProductGateway()

    repository = ConcreteProductRepository(product_gateway=gateway)
    get_list = repository.get_list()
    assert (
        get_list,
        [product]
    )


def test_create(mocker):
    mocker.patch.object(ProductGateway, 'create')

    gateway = ProductGateway()
    repository = ConcreteProductRepository(product_gateway=gateway)
    repository.create("sku", "test", 22.0, "brand")

    gateway.create.assert_called_with("sku", "test", 22.0, "brand")


def test_delete(mocker):
    mocker.patch.object(ProductGateway, 'delete')

    gateway = ProductGateway()
    repository = ConcreteProductRepository(product_gateway=gateway)
    repository.delete(1)

    gateway.delete.assert_called_with(1)


def test_edit(mocker):
    mocker.patch.object(ProductGateway, 'edit')

    gateway = ProductGateway()
    repository = ConcreteProductRepository(product_gateway=gateway)
    repository.edit(1, "sku", "test", 22.0, "brand")

    gateway.edit.assert_called_with(1, "sku", "test", 22.0, "brand")
