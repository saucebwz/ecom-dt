from django.conf.urls import patterns, url
from cart import views

urlpatterns = patterns('',
                       url('^$', views.cart_view, name='cart_view'),
)
