import json

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

from repository.db_gateway import DataBaseGateway
from repository.product_repository import ConcreteProductRepository
from rest.product_request import ProductRequest
from service.product_service import ProductService

app = Flask(__name__)

auth = HTTPBasicAuth()

gateway = DataBaseGateway()
repository = ConcreteProductRepository(product_gateway=gateway);
product_service = ProductService(product_repository=repository)


@auth.verify_password
def verify_password(username, password):
    app.logger.info(username)
    app.logger.info(password)
    return gateway.verifyPassword(username, password)


@app.route("/")
def list():
    return jsonify(product_service.get_list())


@app.route('/', methods=['POST'])
@auth.login_required
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
