from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def custom_function(Myclass):

	most_recent_categories = Category.objects.all()[:3]
	new_stuff = Myclass.objects.filter(condition='Nouveauté')
	used_stuff = Myclass.objects.filter(condition='Usagé')
	old_stuff = Myclass.objects.filter(condition='Ancien')


	new_stuff_condition = []
	used_stuff_condition = []
	old_stuff_condition = []

	for y in used_stuff:
		used_stuff_condition.append(y.condition)

	for x in new_stuff:
		new_stuff_condition.append(x.condition)

	for z in old_stuff:
		old_stuff_condition.append(z.condition)

	new = new_stuff_condition[0]
	used = used_stuff_condition[0]
	old = old_stuff_condition[0]

	return (new, used, old, most_recent_categories)


def store(request, category_slug=None):

	categories = None
	product = None


	new, used, old, most_recent_categories = custom_function(Product)


	if category_slug:
		categories = get_object_or_404(Category, slug=category_slug)
		product = Product.objects.filter(is_available=True, category=categories)
		paginator = Paginator(product, 4)
		page = request.GET.get('page')
		paged_products = paginator.get_page(page)
		product_count = product.count()
	else:
		product = Product.objects.all().filter(is_available=True).order_by('id')
		paginator = Paginator(product, 4)
		page = request.GET.get('page')
		paged_products = paginator.get_page(page)
		product_count = product.count() 

	template_name = 'store/store.html'
	context = {
		'most_recent_categories':most_recent_categories,
		'available_product': paged_products,
		'product_count': product_count,
		'new' : new,
		'used' : used,
		'old' : old,

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


def search(request):

	new, used, old, most_recent_categories = custom_function(Product)
	products = None
	product_count=0

	# if products is None:
	# 	return HttpResponseRedirect()

	if 'q' in request.GET:
		keyword = request.GET['q']
		if keyword:
			products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword) | Q(description__iexact=keyword) )
			product_count = products.count()

	template_name = 'store/store.html'
	context = {
		'available_product' : products,
		'product_count' : product_count,
		'most_recent_categories':most_recent_categories,
		'old':old,
		'new':new,
		'used':used,
	}

	return render(request, template_name, context)

