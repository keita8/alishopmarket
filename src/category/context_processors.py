from .models import Category
from store.models import Banner

def category_list(request):
	categories = Category.objects.all()
	banner_image1 = Banner.objects.first()
	banner_image2 = Banner.objects.last()

	return dict(categories=categories, banner_image1=banner_image1, banner_image2=banner_image2)