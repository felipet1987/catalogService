import json

from flask import Flask, jsonify, request

from gateway.product_gateway import ProductGateway
from repository.product_repository import ConcreteProductRepository
from rest.product_request import ProductRequest
from service.product_service import ProductService

app = Flask(__name__)
gateway = ProductGateway()
repository = ConcreteProductRepository(product_gateway=gateway);
product_service = ProductService(product_repository=repository)
gateway.create_table()


@app.route("/")
def list():
    return jsonify(product_service.get_list())


@app.route('/', methods=['POST'])
def create():
    data = json.loads(request.data)

    product_request = ProductRequest(
        data.get("sku"),
        data.get("name"),
        data.get("price"),
        data.get("brand")
    )
    product_service.create(product_request)

    return ""


@app.route('/<product_id>', methods=['POST'])
def edit(product_id):
    data = json.loads(request.data)
    product_request = ProductRequest(
        data.get("sku"),
        data.get("name"),
        data.get("price"),
        data.get("brand")
    )

    product_service.edit(product_id, product_request)
    return ""


@app.route('/<product_id>', methods=['DELETE'])
def delete(product_id):
    product_service.delete(product_id)
    return ""



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
