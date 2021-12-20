# Generated by Django 3.2.4 on 2021-12-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=80, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=80, verbose_name='Prenom')),
                ('username', models.CharField(max_length=80, unique=True, verbose_name="Nom d'utilisateur")),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='Email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Compte crée')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Dernière connexion')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin ?')),
                ('is_active', models.BooleanField(default=False, verbose_name='Compte activé ?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Membre ?')),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Super administrateur ?')),
            ],
            options={
                'verbose_name': 'compte utilisateur',
                'verbose_name_plural': 'compte utilisateur',
            },
        ),
    ]
