from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('email', 'last_name', 'first_name', 'username', 'last_login', 'date_joined', 'is_active')
	filter_horizontal = ()
	readonly_fields = ('last_login', 'date_joined')
	list_display_links = ('email', 'last_name', 'first_name', 'username')
	list_filter = ('email', 'last_name', 'first_name', 'username')
	fieldsets = ()
	ordering = ('-date_joined', )

admin.site.register(Account, AccountAdmin)