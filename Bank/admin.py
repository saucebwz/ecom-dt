from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Bank.forms import UserForm, UserChangeForm
from Bank.models import MyBankUser, Category, Product


#class BankUserAdmin(admin.ModelAdmin):
#    list_display = ('username', 'money')
#admin.site.register(BankUser, BankUserAdmin)

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserForm
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('first_name', 'second_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    list_display = ('email', )
    list_filter = ('is_active', )
    search_fields = ('first_name', 'second_name', 'email')
    ordering = ('email',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', )
    list_display_links = ('name', )
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description']
    exclude = ('created_at', )

    prepopulated_fields = {'slug': ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', )
    list_display_links = ('name', )
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'quantity']
    exclude = ('created_at', )
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(MyBankUser, MyUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)