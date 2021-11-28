from django.db import models
from category.models import Category
from django.shortcuts import reverse, render


# Create your models here.
class Product(models.Model):

	product_name = models.CharField(max_length=200, verbose_name="Article")
	slug = models.SlugField(max_length=200)
	description = models.TextField()
	price = models.IntegerField(verbose_name='Prix', default=0)
	image = models.ImageField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categorie de l\'article')
	stock = models.IntegerField(default=0)
	is_available = models.BooleanField(default=True, verbose_name='Disponible ?')
	created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")
	modified_date = models.DateTimeField(auto_now=True,verbose_name='Modifié le')

	class Meta:
		ordering = ['-created_date']
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	def get_url(self):
		return reverse('store:product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.product_name