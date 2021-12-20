from django.db import models
from store.models import Product, Variation
from accounts.models import Account
# Create your models here.
class Cart(models.Model):

	cart_id = models.CharField(max_length=250, blank=True, verbose_name='Panier')
	date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date de creation du panier")

	class Meta:
		verbose_name = 'Panier'
		verbose_name_plural = 'Paniers'


	def __str__(self):
		return self.cart_id


class CartItem(models.Model):

	user       = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, verbose_name='Utilisateur')
	product    = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Article')
	cart       = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Panier', null=True)
	variations = models.ManyToManyField(Variation, blank=True, verbose_name='Caracteristiques')
	quantity   = models.IntegerField(verbose_name='quantité')
	is_active  = models.BooleanField(verbose_name='Article du panier actif ?' ,default=True)

	class Meta:
		verbose_name = 'Article au panier'
		verbose_name_plural = 'Articles au panier'

	def sub_total(self):
		return self.product.price * self.quantity

	def __unicode__(self):
		return self.product



# class CartItem(models.Model):
# 	product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Article du panier')
# 	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Panier associé à cet article')
# 	variations = models.ManyToManyField(Variation, verbose_name='Caracteristiques')
# 	quantity = models.IntegerField(verbose_name='Quantité')
# 	is_active = models.BooleanField(verbose_name='Panier actif', default=True)

# 	class Meta:
# 		verbose_name = 'Article du panier'
# 		verbose_name_plural = 'Articles du panier'

# 	def sub_total(self):
# 		return (self.product.price * self.quantity)

# 	def __str__(self):
# 		return str(self.product)