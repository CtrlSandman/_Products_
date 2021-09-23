import json
from producer.base_producer import BaseProducer


class ProductProducer(BaseProducer):

    def __init__(self, args):
        super().__init__(args)

    def send_record(self, key: str, value: json):
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            print(f'Exception while producing record value - {value} to topic - {self.topic}: {e}')
        else:
            print(f'Record value - {value} successfully produced to topic - {self.topic}')

    def send_records(self, products: list):
        for product in products:
            self.send_record(key=product.barcode, value=product.to_json())
        self.producer.flush()
