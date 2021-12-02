from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class MyAccountManager(BaseUserManager):

	def create_user(self, first_name, last_name, username, email, password=None):

		if not email:
			raise ValueError('Vous devez fournir une adresse email')
		
		if not first_name:
			raise ValueError("Le nom d'utilisateur est requis.")

		user = self.model(

			email = self.normalize_email(email),
			username = username,
			first_name = first_name,
			last_name = last_name

			)

		user.set_password(password)
		user.save(using=self._db)


		return user


	def create_superuser(self, first_name, last_name, username, email, password):
		user = self.create_user(

			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			username = username,
			password = password,

			)

		user.is_active     = True
		user.is_admin      = True
		user.is_staff      = True
		user.is_superadmin = True

		user.save(using=self._db)

		return user





class Account(AbstractBaseUser):
	first_name = models.CharField(max_length=80, verbose_name='Nom')
	last_name  = models.CharField(max_length=80, verbose_name='Prenom')
	username   = models.CharField(max_length=80, unique=True, verbose_name="Nom d'utilisateur")
	email      = models.CharField(max_length=200, unique=True, verbose_name='Email')
	# phone      = models.CharField(max_length=20, verbose_name='Telephone')
	# phone      = PhoneNumberField()


	# required
	date_joined   = models.DateTimeField(auto_now_add=True, verbose_name='Compte crée')
	last_login    = models.DateTimeField(auto_now_add=True, verbose_name="Dernière connexion")
	is_admin      = models.BooleanField(default=False, verbose_name="admin ?")
	is_active     = models.BooleanField(default=False,verbose_name="Compte activé ?")
	is_staff      = models.BooleanField(default=False, verbose_name="Membre ?")
	is_superadmin = models.BooleanField(default=False, verbose_name="Super administrateur ?")

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	objects = MyAccountManager()

	class Meta:
		verbose_name = 'compte utilisateur'
		verbose_name_plural = 'compte utilisateur'


	def __str__(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, add_label):
		return True