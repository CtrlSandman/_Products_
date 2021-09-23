from faker import Faker
import faker_commerce
import random


class Product(object):

    def __init__(self, barcode: str, category: str, product_name: str, color: str, material: str, price: float):
        self.barcode = barcode
        self.category = category
        self.product_name = product_name
        self.color = color
        self.material = material
        self.price = price

    def to_json(self) -> dict:
        return self.__dict__

    @staticmethod
    def generate_rand_product():
        fake = Faker()
        fake.add_provider(faker_commerce.Provider)
        price100 = random.randint(100, 100000)
        return Product(
            barcode=fake.ean(length=13),
            category=fake.ecommerce_category(),
            product_name=fake.ecommerce_name(),
            color=fake.color_name(),
            material=fake.random_element(elements=('metal', 'plastic', 'rubber', 'glass')),
            price=round(price100/100, 2)
        )
