from django.urls import path
from . import views

app_name = 'store'


urlpatterns = [

	path('', views.store, name='shop'),
	path('<slug:category_slug>/', views.store, name='product_by_category'),
	path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

]