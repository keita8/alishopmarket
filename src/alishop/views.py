from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):

	product = Product.objects.filter(is_available=True)

	template_name = 'pages/home.html'
	context = {
		'product' : product,
	}

	return render(request, template_name, context)