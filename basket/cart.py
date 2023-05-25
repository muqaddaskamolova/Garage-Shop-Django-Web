from django.http import request
from decimal import Decimal
from django.conf import settings

from store.models import Product


class Basket(object):
    """
    Base basket class, providing some default behaviors that can be inherited or overrided as necessary
    """

    def __init__(self):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if 'session_key' not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, product_qty, override_quantity=False):
        """Adding and updating users basket session data"""
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': int(product_qty), 'price': str(product.price)}
        if override_quantity:
            self.basket[product_id]['quantity'] = product_qty
        else:
            self.basket[product_id]['quantity'] += product_qty
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.basket.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['productqty']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.basket.values())

    def update(self, product, product_qty):
        """
        Update a product in the cart.
        """
        product_id = product
        product_qty = product_qty
        if product_id not in self.basket:
            self.basket[product_id]['product_qty'] = product_qty
        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        subtotal = sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(subtotal)

        total = subtotal + Decimal(shipping)

        return total

    def delete(self, product):
        """
        Remove a product from the cart.
        """
        product_id = product
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.BASKET_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
