from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def custom_function(Myclass):


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

	return (new, used, old)


def home(request):

	product = Product.objects.all().filter(is_available=True)

	new, used, old = custom_function(Product)

	template_name = 'pages/home.html'
	context = {

		'product' : product,
		'new' : new,
		'used':used,
		'old': old,
	}

	return render(request, template_name, context)