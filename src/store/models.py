from django.db import models
from category.models import Category
from django.shortcuts import reverse, render
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Product(models.Model):

    features_choices=(
		('Cruise Control', 'Cruise Control'),
		('Audio Interface', 'Audio Interface'),
		('Airbags', 'Airbags'),
		('Air Conditioning', 'Air Conditioning'),
		('Seat Heating', 'Seat Heating'),
		('Alarm System', 'Alarm System'),
		('ParkAssist', 'ParkAssist'),
		('Power Steering', 'Power Steering'),
		('Reversing Camera', 'Reversing Camera'),
		('Direct Fuel Injection', 'Direct Fuel Injection'),
		('Auto Start/Stop', 'Auto Start/Stop'),
		('Wind Deflector', 'Wind Deflector'),
		('Bluetooth Handset', 'Bluetooth Handset'),
    )


    state_choice = (
        ('GN', 'GUINEE'),
        ('US', 'USA'),
        ('FR', 'FRANCE'),
        ('MA', 'MAROC'),
        ('CA', 'CANADA'),
        ('BR', 'BRESIL'),
        ('AR', 'ARGENTINE'),
        ('DE', 'ALLEMAGNE'),
        ('IT', 'ITALIE'),
        ('ES', 'ESPAGNE'),
        ('PT', 'PORTUGAL'),
        ('RU', 'RUSSIE'),
        ('IN', 'INDE'),
        ('ID', 'INDONESIE'),
        ('IN', 'Indiana'),
        ('MY', 'MALAYSIE'),
        ('CN', 'CHINE'),
        ('JP', 'JAPON'),
        ('UK', 'ANGLETERRE'),
        ('NL', 'PAYS BAS'),
        ('BE', 'BELGIQUE'),
    )



    condition_choice = (

    	('Nouveauté', 'Nouveauté'),
    	('Usagé','Usagé'),
    	('Ancien','Ancien')
    )

    year_choice = []

    for r in range(2000, (datetime.now().year+1)):
    	year_choice.append((r,r))

    product_name  = models.CharField(max_length=200, verbose_name="Article")
    slug          = models.SlugField(max_length=200)
    # brand         = models.CharField(max_length=200, verbose_name='Marque', blank=True)
    description   = RichTextField()
    manufacturer  = models.CharField(choices=state_choice, max_length=50, blank=True, verbose_name='Fabricant')
    condition     = models.CharField(choices=condition_choice, max_length=200, blank=True)
    year          = models.IntegerField(('Année'), choices=year_choice, default='2021')
    price         = models.IntegerField(verbose_name='Prix', default=0)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categorie de l\'article')
    features      = MultiSelectField(choices=features_choices, blank=True, verbose_name='Caracteristiques')
    image         = models.ImageField()
    image1        = models.ImageField(blank=True)
    image2        = models.ImageField(blank=True)
    image3        = models.ImageField(blank=True)
    image4        = models.ImageField(blank=True)
    stock         = models.IntegerField(default=0)
    # new_item      = models.BooleanField(default=False, verbose_name='Nouveauté ?')
    is_available  = models.BooleanField(default=True, verbose_name='Disponible ?')
    free_shipping = models.BooleanField(default=False, verbose_name='Livraison gratuite ?')
    created_date  = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")
    modified_date = models.DateTimeField(auto_now=True,verbose_name='Modifié le')

    class Meta:
    	ordering = ['-created_date']
    	verbose_name = 'Article'
    	verbose_name_plural = 'Articles'

    def get_url(self):
    	return reverse('store:product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
    	return self.product_name