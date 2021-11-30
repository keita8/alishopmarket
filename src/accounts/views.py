from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from carts.views import _cart_id
from carts.models import Cart, CartItem
import requests

# Connexion
def login(request):

	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		user = auth.authenticate(email=email, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Votre email ou votre mot de passe est incorrecte')
			return render(request, 'accounts/login.html')
	else:
		return render(request, 'accounts/login.html')

# Déconnexion
@login_required(login_url = 'accounts:login')
def logout_user(request):
	auth.logout(request)
	messages.success(request, 'Vous êtes deconnecté.')
	return redirect('accounts:login')

# Inscription
def register(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                first_name   = form.cleaned_data['first_name']
                last_name    = form.cleaned_data['last_name']
                phone        = form.cleaned_data['phone']
                email        = form.cleaned_data['email']
                password     = form.cleaned_data['password']
                username     = email.split('@')[0]
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.phone = phone
                user.save()

                # LIEN D'ACTIVATION DU COMPTE
                current_site = get_current_site(request)
                mail_subject = "Lien d'activation de votre compte"
                message      = render_to_string('accounts/account_verification_email.html', {
                    'user'   : user,
                    'domain' : current_site,
                    'uid'    : urlsafe_base64_encode(force_bytes(user.pk)),
                    'token'  : default_token_generator.make_token(user),
                    } )
                to_email=email
                send_email=EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                # messages.success(request, "Compte crée avec succès")
                # return redirect('accounts:login')
                return redirect('/accounts/login/?command=verification&email='+email)

        else:
            form = RegistrationForm()

        context = {
        'form' : form,
        }
        return render(request, 'accounts/register.html', context)

# Lien d'activation du compte
def activate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Votre compte a bien été activé')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Ce lien d\'activation a deja expiré.')
        return redirect('accounts:register')

