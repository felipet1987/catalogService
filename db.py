from gateway.product_gateway import ProductGateway

if __name__ == "__main__":
    gateway = ProductGateway()
    gateway.create_table()
    print("db ready")


