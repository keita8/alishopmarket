from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
	list_display = ['product', 'cart', 'is_active', 'quantity']
	list_display_links = ['product']

class CartAdmin(admin.ModelAdmin):
	list_display = ['cart_id', 'date_added']
	list_display_links = ['cart_id']
	
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
