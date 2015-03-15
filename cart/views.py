from django.shortcuts import render
from cart import cart
from django.shortcuts import render_to_response
from django.template import RequestContext


def cart_view(request):
    cart_items = cart.get_cart_items(request)
    cart_item_count = cart.cart_item_count(request)
    return render_to_response('cart.html', {'cart_item_count': cart_item_count, 'cart_items':cart_items}, context_instance=RequestContext(request))
