from django.contrib import admin
from .models import Product, Banner, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'price', 'stock', 'category', 'condition', 'is_available', 'free_shipping', 'created_date']
	prepopulated_fields = {'slug' : ('product_name', )}
	list_editable = ['is_available', 'free_shipping']
	search_fields = ['product_name', 'price']



class VariationAdmin(admin.ModelAdmin):
	list_display = ('product', 'variation_category', 'variation_value', 'is_active')
	list_filter = ('product', 'variation_category', 'variation_value', 'is_active')
	list_editable = ('is_active', )



admin.site.register(Product, ProductAdmin)
admin.site.register(Banner)
admin.site.register(Variation, VariationAdmin)