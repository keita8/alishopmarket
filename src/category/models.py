from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=80, verbose_name='Categorie')
	slug= models.SlugField(max_length=80)
	description = models.TextField()
	category_image = models.ImageField(verbose_name='Image de la categorie', upload_to='photos/categories')

	class Meta:
		verbose_name = 'Categorie'
		verbose_name_plural = 'Categories'

	def get_url(self):
		return reverse('store:product_by_category', args=[self.slug])


	def __str__(self):
		return self.category_name