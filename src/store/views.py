from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_slug=None):

	categories = None
	product = None

	if category_slug:
		categories = get_object_or_404(Category, slug=category_slug)
		product = Product.objects.filter(is_available=True, category=categories)
		product_count = product.count()
	else:
		product = Product.objects.filter(is_available=True)
		product_count = product.count() 

	template_name = 'store/store.html'
	context = {

		'store_product': product,
		'product_count': product_count,
	}

	return render(request, template_name, context)


def product_detail(request, category_slug, product_slug):

	try:
		single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
	except Exception as e:
		raise e
	else:
		pass
	finally:
		pass

	template_name = 'store/product_detail.html'
	context = {
		'single_product':single_product,
	}

	return render(request, template_name, context)
