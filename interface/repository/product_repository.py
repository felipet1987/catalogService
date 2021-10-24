class ProductRepository():
    async def get_list(self):
        raise NotImplementedError

    async def create(self, name):
        raise NotImplementedError

    async def delete(self, product_id):
        raise NotImplementedError

    async def edit(self, product_id, name):
        raise NotImplementedError
