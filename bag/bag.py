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
        
        if update_quantity:
            self.bag[product_id]['quantity'] = quantity
        else:
            self.bag[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """Ensure prices are stored as floats for JSON compatibility."""
        for item in self.bag.values():
            item['price'] = float(item['price'])
        self.session[settings.BAG_SESSION_ID] = self.bag
        self.session.modified = True

    def remove(self, product):
        """Remove product from the bag."""
        product_id = str(product.id)
        if product_id in self.bag:
            del self.bag[product_id]
            self.save()

    def __iter__(self):
        """Retrieve actual product objects and avoid storing them in the session."""
        product_ids = self.bag.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            product_id = str(product.id)
            item = {
                'product': product,
                'quantity': self.bag[product_id]['quantity'],
                'price': self.bag[product_id]['price'],
                'total_price': self.bag[product_id]['quantity'] * self.bag[product_id]['price']
            }
            yield item

    def __len__(self):
        """Count total quantity of items in the bag."""
        return sum(item['quantity'] for item in self.bag.values())

    def get_total_price(self):
        """Calculate total bag price."""
        return float(sum(item['price'] * item['quantity'] for item in self.bag.values()))

    def clear(self):
        """Remove all items from the bag."""
        self.session.pop(settings.BAG_SESSION_ID, None)
        self.session.modified = True

    def sanitize_session(self):
        """Ensure that all items in the session are correctly formatted."""
        for product_id, item in self.bag.items():
            item.setdefault('quantity', 1)  
            item.setdefault('price', 0.0)  
            item['price'] = float(item['price'])  
