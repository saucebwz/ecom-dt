from django.shortcuts import render
from cart import cart
from django.shortcuts import render_to_response
from django.template import RequestContext
from Bank.models import Category



def cart_view(request):
    if request.method == "POST":
        postdata = request.POST.copy()
        if postdata['submit'] == 'Update':
            item_id = postdata['item_id']
            quantity = postdata['quantity']
            item = cart.get_item(request, item_id)
            if item:
                if int(quantity) > 0:
                    item.quantity = int(quantity)
                    item.save()
        elif postdata['submit'] == 'Delete':
            item_id = postdata['item_id']
            item = cart.get_item(request, item_id)
            if item:
                item.delete()

    cart_items = cart.get_cart_items(request)
    cart_item_count = cart.cart_item_count(request)
    total_sum = cart.get_full_price(request)
    categories = Category.objects.filter(is_active=True)
    return render_to_response('cart.html', {'cart_item_count': cart_item_count, 'cart_items':cart_items, 'categories': categories, 'total_sum': total_sum}, context_instance=RequestContext(request))

