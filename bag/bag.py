from django.conf import settings
from products.models import Product

class Bag:
    """Manages the shopping bag and handles session storage."""

    def __init__(self, request):
        """Initialises the bag, retrieving it from the session or creating a new one."""
        self.session = request.session
        self.bag = self.session.get(settings.BAG_SESSION_ID, {})
        self.sanitize_session()

    def add(self, product, quantity=1, update_quantity=False):
        """Adds a product to the bag or updates its quantity."""
        product_id = str(product.id)
        if product_id not in self.bag:
            self.bag[product_id] = {'quantity': 0, 'price': float(product.price)}

        if update_quantity:
            self.bag[product_id]['quantity'] = int(quantity)
        else:
            self.bag[product_id]['quantity'] += int(quantity)

        self.save()

    def save(self):
        """Saves changes to the session."""
        for item in self.bag.values():
            item['price'] = float(item['price'])  # Ensure price is stored as a float
        self.session[settings.BAG_SESSION_ID] = self.bag
        self.session.modified = True

    def remove(self, product):
        """Removes a product from the bag."""
        product_id = str(product.id)
        if product_id in self.bag:
            del self.bag[product_id]
            self.save()

    def __iter__(self):
        """Yields product objects along with their quantities and prices."""
        product_ids = self.bag.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            product_id = str(product.id)
            yield {
                'product': product,
                'quantity': self.bag[product_id]['quantity'],
                'price': self.bag[product_id]['price'],
                'total_price': self.bag[product_id]['quantity'] * self.bag[product_id]['price']
            }

    def __len__(self):
        """Returns the total number of items in the bag."""
        return sum(item['quantity'] for item in self.bag.values())

    def get_total_price(self):
        """Calculates the total price of all items in the bag."""
        return float(sum(item['price'] * item['quantity'] for item in self.bag.values()))

    def clear(self):
        """Empties the shopping bag."""
        self.session.pop(settings.BAG_SESSION_ID, None)
        self.session.modified = True

    def sanitize_session(self):
        """Ensures session data is properly formatted."""
        if not isinstance(self.bag, dict):
            self.bag = {}

        for item in self.bag.values():
            item.setdefault('quantity', 1)
            item.setdefault('price', 0.0)
            item['price'] = float(item['price'])

        self.session[settings.BAG_SESSION_ID] = self.bag
        self.session.modified = True
