from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# Creation d'une session (id) associée à un panier
def _cart_id(request):

	cart = request.session.session_key

	if not cart:
		cart = request.session.create()

	return cart


# panier
def cart(request, total=0, quantity=0, cart_items=None):
	
	try:

		tax = 0 
		grand_total = 0
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart, is_active=True)

		for cart_item in cart_items:

			total += (cart_item.product.price * cart_item.quantity)
			quantity += cart_item.quantity

		tax = (2 * total) / (100)
		grand_total = total + tax

	except ObjectDoesNotExist:
		pass

	context = {

		'total': total,
		'quantity' : quantity,
		'cart_items' : cart_items,
		'taxt'		 : tax,
		'grand_total': grand_total,
	}

	template_name = 'store/cart.html'

	return render(request, template_name, context)

# ajouter un article à un panier
def add_cart(request, product_id):

	product = Product.objects.get(pk=product_id)
	product_variation = []


	if request.method == "POST":
		for item in request.POST:
			key = item
			value = request.POST[key]

			try:
				variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
				product_variation.append(variation)
			except:
				pass



	try:
		cart = Cart.objects.get(cart_id=_cart_id(request)) # recupère le panier utilisant la session id
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
			cart_id = _cart_id(request)
		) 

	cart.save()

	try:
		cart_item = CartItem.objects.get(product=product, cart=cart)

		if len(product_variation) > 0:
			for item in product_variation:
				cart_item.variations.add(item)
		cart_item.quantity += 1
		cart_item.save()

	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
			product=product, cart=cart, quantity=1
			)

		if len(product_variation) > 0:
			for item in product_variation:
				cart_item.variations.add(item)

		cart_item.save()

	return redirect('carts:carts')


# décrementer la quantité d'un article
def remove_cart(request, product_id):

	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)

	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()

	return redirect('carts:carts')


# retirer un article du panier
def remove_cart_item(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)

	cart_item.delete()

	return redirect('carts:carts')


def checkout(request):

	template_name = 'carts/checkout.html'
	context = {
	
	}

	return render(request, template_name, context)





















