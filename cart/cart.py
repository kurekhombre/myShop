from django.conf import settings

from product.models import Product


class Cart(object):
    """
    The Cart class is a subclass of the object class. It has a constructor that takes a request object
    as a parameter. The constructor initializes the session and cart variables. The cart variable is a
    dictionary that stores the product id and quantity of each product in the cart. The __iter__ method
    iterates through the cart dictionary and adds the product object to each item in the cart. The
    __len__ method returns the total number of items in the cart. The save method saves the cart to the
    session. The add method adds a product to the cart. The remove method removes a product from the
    cart. The get_total_cost method returns the total cost of the items in the cart.
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity']) / 100

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values())) / 100

    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None