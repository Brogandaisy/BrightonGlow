from decimal import Decimal
from django.conf import settings
from products.models import Product

class Bag:
    def __init__(self, request):
        self.session = request.session
        bag = self.session.get(settings.BAG_SESSION_ID)
        if not bag:
            bag = self.session[settings.BAG_SESSION_ID] = {}
        self.bag = bag

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.bag:
            self.bag[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.bag[product_id]['quantity'] = quantity
        else:
            self.bag[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.bag:
            del self.bag[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.bag.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.bag[str(product.id)]['product'] = product
        for item in self.bag.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.bag.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.bag.values())

    def clear(self):
        del self.session[settings.BAG_SESSION_ID]
        self.save()