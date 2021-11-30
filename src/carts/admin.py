from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemAdmin(admin.ModelAdmin):

	list_display = ['product', 'cart', 'is_active', 'quantity']
	list_display_links = ['product']


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
