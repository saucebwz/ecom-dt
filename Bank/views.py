from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from Bank.forms import UserForm
from Bank.models import MyBankUser
from django.views.generic import View
from Bank.models import Category, Product
from django.shortcuts import get_object_or_404
from cart.forms import AddProductToCartForm
from cart import cart




def loginprocess(request):
    logout(request)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('main'))
    return render_to_response('login.html', {'error': password},
                              context_instance=RequestContext(request))


def login_page(request):
    return render_to_response('login.html', context_instance=RequestContext(request))


#@login_required(login_url=reverse_lazy('login_page'))
def main_view(request):
    categories = Category.objects.filter(is_active=True)
    all = categories.get(name="All")
    return render_to_response('main.html', {#'user': MyBankUser.objects.get(pk=request.user.id)
                                            'categories': categories,
                                            'all_category': all}, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))


class reg_view(View):
    form_class = UserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('login.html', context_instance=RequestContext(request))
        else:
            return render_to_response('register.html', {'user_form': form}, context_instance=RequestContext(request))

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'register.html', {'user_form': form})


def category_view(request, category_slug):
    all_categories = Category.objects.all()
    category = all_categories.get(slug=category_slug)
    products = category.product_set.all()
    return render_to_response('category.html', {'category': category, 'products': products, 'categories': all_categories},
                              context_instance=RequestContext(request))


def product_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = AddProductToCartForm(request, postdata)
        if form.is_valid():
            ss = cart.add_to_cart(request)
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(reverse('cart_view'))
    else:
        form = AddProductToCartForm(request, label_suffix=":")

    form.fields['product_slug'].widget.attrs['value'] = product_slug
    request.session.set_test_cookie()
    return render_to_response('product.html', {'product': product, 'form': form}, context_instance=RequestContext(request))


