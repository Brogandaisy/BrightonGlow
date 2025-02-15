from django.conf import settings
from products.models import Product

class Bag:
    def __init__(self, request):
        self.session = request.session
        self.bag = self.session.get(settings.BAG_SESSION_ID, {})
        self.sanitize_session()

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.bag:
            self.bag[product_id] = {'quantity': 0, 'price': float(product.price)}
        
        self.bag[product_id]['quantity'] = quantity if update_quantity else self.bag[product_id]['quantity'] + quantity
        self.save()

    def save(self):
        for item in self.bag.values():
            item['price'] = float(item['price'])
        self.session[settings.BAG_SESSION_ID] = self.bag
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        self.bag.pop(product_id, None)
        self.save()

    def __iter__(self):
        products = Product.objects.filter(id__in=self.bag.keys())
        for product in products:
            self.bag[str(product.id)]['product'] = product
            item = self.bag[str(product.id)]
            item['total_price'] = float(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.bag.values())

    def get_total_price(self):
        return float(sum(float(item['price']) * item['quantity'] for item in self.bag.values()))
    
    def clear(self):
        self.session.pop(settings.BAG_SESSION_ID, None)
        self.session.modified = True

    def sanitize_session(self):
        for item in self.bag.values():
            item['price'] = float(item.get('price', 0))
