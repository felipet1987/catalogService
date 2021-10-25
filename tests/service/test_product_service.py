from service.product_repository import ProductRepository
from rest.product_request import ProductRequest
from service.product_service import ProductService

request = ProductRequest("sku", "test", 22.0, "brand")


def test_get(monkeypatch):
    product = {"id": 1, "sku": "sku", "name": "test","price": 22.0,"brand":"brand"}

    products = [product]

    def mock_get(*args, **kwargs):
        return products

    monkeypatch.setattr(ProductRepository, "get_list", mock_get)

    repo = ProductRepository()

    service = ProductService(product_repository=repo)

    get_list = service.get_list()
    assert get_list, products


def test_create(mocker):
    mocker.patch.object(ProductRepository, 'create')

    repo = ProductRepository()
    service = ProductService(product_repository=repo)

    service.create(request)

    repo.create.assert_called_with("sku", "test", 22.0, "brand")


def test_delete(mocker):
    mocker.patch.object(ProductRepository, 'delete')

    repo = ProductRepository()
    service = ProductService(product_repository=repo)
    service.delete(1)

    repo.delete.assert_called_with(1)


def test_edit(mocker):
    mocker.patch.object(ProductRepository, 'edit')

    repo = ProductRepository()
    service = ProductService(product_repository=repo)
    service.edit(1, request)

    repo.edit.assert_called_with(1, "sku", "test", 22.0, "brand")
