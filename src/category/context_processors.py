from .models import Category

def category_list(request):
	categories = Category.objects.all()
	return dict(categories=categories)