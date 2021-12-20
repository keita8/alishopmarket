from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# def custom_function(Myclass):
# 	new_stuff = Myclass.objects.filter(condition='New')
# 	new_stuff_condition = []


# 	for x in new_stuff:
# 		new_stuff_condition.append(x.condition)
# 	new = new_stuff_condition[0]
# 	return new



def home(request):

	product = Product.objects.all().filter(is_available=True)

	# new = custom_function(Product)

	template_name = 'pages/home.html'
	context = {

		'product' : product,
		# 'new' : new,
	}

	return render(request, template_name, context)