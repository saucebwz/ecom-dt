import random
from cart.models import CartItem
from django.shortcuts import get_object_or_404
from Bank.models import Product
ID_KEY = 'card_id_key'

def _cart_id(request):
    if request.session.get(ID_KEY, '') == '':
        request.session[ID_KEY] = generate_id()
    return request.session[ID_KEY]


def generate_id():
    STR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()';
    id = ''
    length = 50
    for y in range(length):
        id += STR[random.randint(0, len(STR) - 1)]
    return id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))


def add_to_cart(request):
    postdata = request.POST.copy()
    product_slug = postdata.get('product_slug', '')
    quantity = postdata.get('quantity', 1)
    p = get_object_or_404(Product, slug=product_slug)
    cart_items = CartItem.objects.filter(cart_id=_cart_id(request))
    product_in_cart = False
    for cart_item in cart_items:
        if cart_item.product.id == p.id:
            cart_item.augment_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        test = _cart_id(request)
        ci.cart_id = test
        ci.save()


def cart_item_count(request):
    return get_cart_items(request).count()



