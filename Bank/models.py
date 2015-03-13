from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.urlresolvers import reverse


#class BankUser(models.Model):
#    user = models.OneToOneField(User)
 #   money = models.IntegerField(blank=True, default=0)
  #  username = models.CharField(blank=True, default="", max_length=20)

   # def __unicode__(self):
    #    return self.user.username
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('catalog', args=(self.slug, ))



class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    #image = models.ImageField(upload_to='media_images/')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    catalog = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('product', args=(self.slug, ))


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        now = timezone.now()
        if not email:
            raise ValueError('The given email address must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, date_joined=now, is_superuser=False, is_staff=False,  **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        u = self.create_user(email, password, **kwargs)
        u.is_superuser = True
        u.is_staff = True
        u.save(using=self._db)
        return u


class MyBankUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=20, blank=True)
    second_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now())
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return ', '.join((self.first_name, self.second_name))





