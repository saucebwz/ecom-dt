from django.db import models
from Bank.models import Product
# Create your models here.

class CartItem(models.Model):
    cart_id = models.CharField(max_length=60)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('Bank.Product', unique=False)

    class Meta:
        ordering = ['-date_added']

    def total_price(self):
        return self.product.price * self.quantity

    def name(self):
        return self.product.name

    def get_full_price(self):
        return str(self.product.price * self.quantity) + "$"

    def price(self):
        return self.product.get_price()

    def image(self):
        return self.product.image

    def get_absolute_url(self):
        self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity += int(quantity)
        self.save()

    def __str__(self):
        if self.cart_id is None:
            return "lol"
        else:
            return str(len(self.cart_id))