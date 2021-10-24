from dataclasses import dataclass


@dataclass
class ProductRequest:
    sku: str
    name: str
    price: float
    brand: str

